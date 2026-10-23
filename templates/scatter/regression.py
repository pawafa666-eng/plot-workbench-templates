"""线性拟合图
数据要求：至少 2 行、2 列数值：x、y；x 不可全部相同。
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
    x = np.linspace(0, 10, 40)
    y = 1 + .7*x + rng.normal(scale=.7, size=40)

if len(x) < 2 or np.ptp(x) == 0:
    raise ValueError("拟合至少需要 2 个不同的 x")
coefficients = np.polyfit(x, y, 1)
line = np.linspace(np.min(x), np.max(x), 100)
ax.scatter(x, y, color="#55a6a0", alpha=.75)
ax.plot(line, np.polyval(coefficients, line), color="#b85e42", label="Linear fit")
ax.legend(frameon=False)
ax.set(xlabel="x", ylabel="y")
fig.tight_layout(pad=0.6)
