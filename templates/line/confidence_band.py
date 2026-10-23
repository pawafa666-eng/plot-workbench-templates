"""置信区间带
数据要求：任意行，4 列数值：x、中心值、下界、上界。
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
    low = data.iloc[:, 2].to_numpy(dtype=float)
    high = data.iloc[:, 3].to_numpy(dtype=float)
else:
    x = np.linspace(0, 6, 50)
    y = 1 + 0.6*x
    low, high = y - 0.4, y + 0.4

ax.fill_between(x, low, high, alpha=.25, color="#276b80", label="Interval")
ax.plot(x, y, color="#276b80", label="Estimate")
ax.legend(frameon=False)
ax.set(xlabel="x", ylabel="Estimate")
fig.tight_layout(pad=0.6)
