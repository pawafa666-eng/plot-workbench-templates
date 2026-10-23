"""面积图
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
    x = np.linspace(0, 6, 50)
    y = 2 + np.sin(x)

ax.fill_between(x, y, color="#55a6a0", alpha=0.4)
ax.plot(x, y, color="#276b80")
ax.set(xlabel="Time", ylabel="Volume")
fig.tight_layout(pad=0.6)
