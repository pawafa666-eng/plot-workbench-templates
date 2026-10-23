"""分组柱状图
数据要求：任意行，3 列：类别、序列 A、序列 B。
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
    a = data.iloc[:, 1].to_numpy(dtype=float)
    b = data.iloc[:, 2].to_numpy(dtype=float)
else:
    labels = np.array(["A", "B", "C", "D"])
    a = np.array([3, 5, 4, 6])
    b = np.array([4, 4, 5, 7])

positions = np.arange(len(labels))
ax.bar(positions-.18, a, width=.36, label="Method A", color="#276b80")
ax.bar(positions+.18, b, width=.36, label="Method B", color="#d39b50")
ax.set_xticks(positions, labels)
ax.set_ylabel("Value")
ax.legend(frameon=False)
fig.tight_layout(pad=0.6)
