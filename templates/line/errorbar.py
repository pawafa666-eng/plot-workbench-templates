"""误差棒图
数据要求：任意行，3 列数值：x、均值、非负误差。
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
    error = data.iloc[:, 2].to_numpy(dtype=float)
else:
    x = np.arange(1, 7)
    y = np.array([2.4, 3.1, 2.9, 4.3, 4.8, 5.5])
    error = np.array([.3, .4, .25, .35, .5, .4])

ax.errorbar(x, y, yerr=error, fmt="o-", capsize=4, color="#276b80")
ax.set(xlabel="Condition", ylabel="Mean ± error")
fig.tight_layout(pad=0.6)
