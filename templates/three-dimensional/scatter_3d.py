"""三维散点图
数据要求：任意行，3 列数值：x、y、z。
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
    z = data.iloc[:, 2].to_numpy(dtype=float)
else:
    x = rng.normal(size=50)
    y = rng.normal(size=50)
    z = .5*x + .3*y + rng.normal(scale=.3, size=50)

fig.delaxes(ax)
ax = fig.add_subplot(111, projection="3d")
ax.scatter(x, y, z, c=z, cmap="viridis", s=25)
ax.set(xlabel="x", ylabel="y", zlabel="z")
ax.view_init(elev=22, azim=-55)
fig.tight_layout(pad=0.6)
