"""箱线图
数据要求：至少 2 行、2 列数值：两组等长样本。
直接运行使用合成示例；在 Plot Workbench 导入数据后自动使用 data。
SPDX-License-Identifier: AGPL-3.0-only
"""
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})
fig, ax = plt.subplots(figsize=(6.4, 4.4))
if "data" in globals() and data is not None:
    a = data.iloc[:, 0].to_numpy(dtype=float)
    b = data.iloc[:, 1].to_numpy(dtype=float)
else:
    a = rng.normal(2, .5, 80)
    b = rng.normal(3, .7, 80)

boxes = ax.boxplot([a, b], tick_labels=["A", "B"], patch_artist=True)
for box, color in zip(boxes["boxes"], ["#55a6a0", "#d39b50"]):
    box.set_facecolor(color)
ax.set(xlabel="Group", ylabel="Value")
fig.tight_layout(pad=0.6)
