"""直方图
数据要求：至少 1 行、1 列数值：样本。
直接运行使用合成示例；在 Plot Workbench 导入数据后自动使用 data。
SPDX-License-Identifier: AGPL-3.0-only
"""
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})
fig, ax = plt.subplots(figsize=(6.4, 4.4))
if "data" in globals() and data is not None:
    y = data.iloc[:, 0].to_numpy(dtype=float)
else:
    y = rng.normal(0, 1, 300)

ax.hist(y, bins="auto", color="#55a6a0", edgecolor="white")
ax.set(xlabel="Value", ylabel="Count")
fig.tight_layout(pad=0.6)
