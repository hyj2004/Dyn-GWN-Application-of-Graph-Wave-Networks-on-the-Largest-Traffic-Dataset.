import argparse
import numpy as np
import pandas as pd
import pickle


def npy2adj_and_id2ind(npy_file_path,sensor_ids, normalized_k=0.1):



    # Builds sensor id to index map.
    sensor_id_to_ind = {}
    for i, sensor_id in enumerate(sensor_ids):
        sensor_id_to_ind[sensor_id] = i

    # 将npy里的adj拿出出来
    adj_mx = np.load(npy_file_path)


    # Sets entries that lower than a threshold, i.e., k, to zero for sparsity.
    adj_mx[adj_mx < normalized_k] = 0
    return sensor_ids, sensor_id_to_ind, adj_mx


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--sensor_ids_filename', type=str, default='/home/dsj22/LargeST-main/dyngwn_meta-la/DynGWN/CA/ca_graph_sensor_ids.txt',
                        help='File containing sensor ids separated by comma.')
    parser.add_argument('--normalized_k', type=float, default=0.1,
                        help='Entries that become lower than normalized_k after normalization are set to zero for sparsity.')
    parser.add_argument('--output_pkl_filename', type=str, default='/home/dsj22/LargeST-main/dyngwn_meta-la/DynGWN/CA/ca_adj.pkl',
                        help='Path of the output file.')
    args = parser.parse_args()

    with open(args.sensor_ids_filename) as f:
        sensor_ids = f.read().strip().split(',')
    normalized_k = args.normalized_k
    npy_file_path = '/home/dsj22/LargeST-main/data/ca/ca_rn_adj.npy'             #你的npy路径
    _, sensor_id_to_ind, adj_mx=  npy2adj_and_id2ind(npy_file_path, sensor_ids, normalized_k)
    print(adj_mx)

    # Save to pickle file.
    with open(args.output_pkl_filename, 'wb') as f:
        pickle.dump([sensor_ids, sensor_id_to_ind, adj_mx], f, protocol=2)
 