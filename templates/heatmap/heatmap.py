"""矩阵热力图
数据要求：任意行，固定 3 列数值矩阵（可自行修改列数）。
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
    c = data.iloc[:, 2].to_numpy(dtype=float)
else:
    a = np.array([1, 2, 4, 3])
    b = np.array([3, 5, 2, 4])
    c = np.array([4, 3, 6, 5])

matrix = np.column_stack([a, b, c])
image = ax.imshow(matrix, cmap="viridis", aspect="auto")
fig.colorbar(image, ax=ax, label="Value")
ax.set_xticks([0, 1, 2], ["A", "B", "C"])
ax.set(xlabel="Column", ylabel="Row")
fig.tight_layout(pad=0.6)
