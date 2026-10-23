"""水平柱状图
数据要求：任意行，2 列：类别、数值。
直接运行使用合成示例；在 Plot Workbench 导入数据后自动使用 data。
SPDX-License-Identifier: AGPL-3.0-only
"""
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})
fig, ax = plt.subplots(figsize=(6.4, 4.4))
if "data" in globals() and data is not None:
    labels = data.iloc[:, 0].astype(str).to_numpy()
    y = data.iloc[:, 1].to_numpy(dtype=float)
else:
    labels = np.array(["North", "South", "East", "West"])
    y = np.array([7, 4, 6, 5])

ax.barh(labels, y, color="#276b80", height=.65)
ax.set(xlabel="Value", ylabel="Group")
fig.tight_layout(pad=0.6)
