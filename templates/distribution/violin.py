"""小提琴图
数据要求：至少 2 行、2 列数值：两组样本，各组应有变化。
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

violins = ax.violinplot([a, b], showmeans=True, showextrema=True)
for body in violins["bodies"]:
    body.set_facecolor("#276b80")
    body.set_alpha(.55)
ax.set_xticks([1, 2], ["A", "B"])
ax.set(xlabel="Group", ylabel="Value")
fig.tight_layout(pad=0.6)
