import numpy as np

# 假设你已经有一个 .npy 文件的路径
npy_file_path = '/home/dsj22/LargeST-main/data/sd/sd_rn_adj.npy'

# 使用 np.load 函数加载 .npy 文件
adj_mx = np.load(npy_file_path)

# 打印加载的邻接矩阵
print(adj_mx)
print(adj_mx.shape)  # 打印矩阵的形状
