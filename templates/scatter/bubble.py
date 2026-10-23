"""气泡图
数据要求：任意行，3 列数值：x、y、气泡大小。
直接运行使用合成示例；在 Plot Workbench 导入数据后自动使用 data。
SPDX-License-Identifier: AGPL-3.0-only
"""
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})
fig, ax = plt.subplots(figsize=(6.4, 4.4))
if "data" in globals() and data is not None:
    x = data.iloc[:, 0].to_numpy(dtype=float)
    y = data.iloc[:, 1].to_numpy(dtype=float)
    size = data.iloc[:, 2].to_numpy(dtype=float)
else:
    x = rng.uniform(0, 10, 25)
    y = rng.uniform(0, 10, 25)
    size = rng.uniform(1, 10, 25)

sizes = 30 + 300*np.abs(size)/max(float(np.max(np.abs(size))), 1e-12)
ax.scatter(x, y, s=sizes, c=size, cmap="viridis", alpha=.65, edgecolors="white")
ax.set(xlabel="x", ylabel="y")
fig.tight_layout(pad=0.6)
