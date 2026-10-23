"""Render each ordinary script in a fresh process using synthetic inputs only."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import runpy
import subprocess
import sys
import tempfile


def render_child(script, destination, case):
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import pandas as pd

    namespace = {}
    if case is not None:
        namespace["data"] = pd.DataFrame(case["values"], columns=case["columns"])
    plt.show = lambda *args, **kwargs: None
    runpy.run_path(str(script), init_globals=namespace, run_name="__main__")
    figures = [plt.figure(number) for number in plt.get_fignums()]
    if len(figures) != 1:
        raise AssertionError(f"Expected one figure, received {len(figures)}")
    figures[0].savefig(destination, dpi=120, facecolor="white")
    plt.close("all")


def verify(write=False):
    from PIL import Image, ImageStat

    root = Path(__file__).resolve().parents[1]
    catalog = json.loads((root / "catalog.json").read_text("utf-8"))
    cases = json.loads((root / "scripts/data_cases.json").read_text("utf-8"))
    assert len(catalog) == 20, "Gallery must contain exactly 20 examples"
    assert len({entry["source"] for entry in catalog}) == len(catalog)
    assert len({entry["preview"] for entry in catalog}) == len(catalog)
    previews = root / "previews"
    if write:
        previews.mkdir(exist_ok=True)
    checks = 0
    with tempfile.TemporaryDirectory(prefix="plot-workbench-gallery-") as temporary:
        temporary = Path(temporary)
        for entry in catalog:
            source = root / entry["source"]
            synthetic = []
            for mode in ("synthetic-a", "synthetic-b", "data"):
                work = temporary / f"{source.stem}-{mode}"
                work.mkdir()
                destination = work / "render.png"
                case_path = work / "case.json"
                if mode == "data":
                    case_path.write_text(json.dumps(cases[entry["id"]]), "utf-8")
                environment = os.environ.copy()
                environment.update(
                    MPLBACKEND="Agg", MPLCONFIGDIR=str(work / "mpl-config"), PYTHONHASHSEED="0"
                )
                command = [sys.executable, str(Path(__file__).resolve()), "--child", str(source), str(destination)]
                if mode == "data":
                    command.append(str(case_path))
                result = subprocess.run(
                    command, cwd=work, env=environment, capture_output=True, timeout=40
                )
                if result.returncode:
                    raise AssertionError(
                        f"{entry['id']} ({mode}) failed:\n"
                        + result.stderr.decode("utf-8", errors="replace")
                    )
                with Image.open(destination) as image:
                    assert image.size == (768, 528), f"Wrong preview size: {entry['id']}"
                    assert max(ImageStat.Stat(image.convert("RGB")).stddev) > 10, (
                        f"Blank preview: {entry['id']}"
                    )
                if mode.startswith("synthetic"):
                    synthetic.append(destination.read_bytes())
                checks += 1
            assert hashlib.sha256(synthetic[0]).digest() == hashlib.sha256(synthetic[1]).digest(), (
                f"Non-deterministic synthetic preview: {entry['id']}"
            )
            preview = root / entry["preview"]
            if write:
                preview.write_bytes(synthetic[0])
            assert preview.is_file(), f"Missing committed preview: {entry['id']}"
            with Image.open(preview) as image:
                assert image.size == (768, 528)
    print(f"Verified {len(catalog)} scripts, {checks} isolated renders, deterministic previews, and 768 x 528 PNGs.")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--child":
        child_case = json.loads(Path(sys.argv[4]).read_text("utf-8")) if len(sys.argv) > 4 else None
        render_child(Path(sys.argv[2]), Path(sys.argv[3]), child_case)
    else:
        parser = argparse.ArgumentParser(description=__doc__)
        parser.add_argument("--write", action="store_true", help="Regenerate committed PNG previews")
        verify(parser.parse_args().write)
