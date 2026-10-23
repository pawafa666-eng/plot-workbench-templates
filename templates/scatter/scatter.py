"""散点图
数据要求：任意行，2 列数值：x、y。
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
else:
    x = rng.normal(size=70)
    y = .8*x + rng.normal(scale=.5, size=70)

ax.scatter(x, y, s=35, color="#276b80", alpha=.7, edgecolors="none")
ax.set(xlabel="x", ylabel="y")
fig.tight_layout(pad=0.6)
