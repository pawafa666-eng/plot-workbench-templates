"""相关系数矩阵
数据要求：至少 3 行、3 列数值：三个变量，各列不可为常数。
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
    a = rng.normal(size=60)
    b = .7*a + rng.normal(scale=.5, size=60)
    c = rng.normal(size=60)

matrix = np.corrcoef(np.column_stack([a, b, c]), rowvar=False)
image = ax.imshow(matrix, cmap="coolwarm", vmin=-1, vmax=1)
fig.colorbar(image, ax=ax, label="Correlation")
for row in range(3):
    for column in range(3):
        ax.text(column, row, f"{matrix[row, column]:.2f}", ha="center", va="center")
ax.set_xticks([0, 1, 2], ["A", "B", "C"])
ax.set_yticks([0, 1, 2], ["A", "B", "C"])
fig.tight_layout(pad=0.6)
