"""经验累积分布
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
    y = rng.normal(3, .8, 100)

ordered = np.sort(y)
probability = np.arange(1, len(y)+1)/len(y)
ax.step(ordered, probability, where="post", color="#276b80", linewidth=2)
ax.set(xlabel="Value", ylabel="Cumulative probability", ylim=(0, 1.02))
fig.tight_layout(pad=0.6)
