import csv

def read_column_from_csv(file_path, column_name):
    with open(file_path, mode='r', encoding='utf-8') as csvfile:
        csvreader = csv.DictReader(csvfile)
        column_data = [row[column_name] for row in csvreader]
        return column_data

def write_column_data_to_string(column_data):
    return ','.join(column_data)

def save_to_txt(file_path, data):
    with open(file_path, mode='w', encoding='utf-8') as txtfile:
        txtfile.write(data)

# 示例用法
csv_file_path = '/home/dsj22/LargeST-main/data/ca/ca_meta.csv'  # 替换成你的CSV文件路径
column_name = 'ID'  # 替换成你要读取的列名
txt_file_path = '/home/dsj22/LargeST-main/dyngwn_meta-la/DynGWN/CA/ca_graph_sensor_ids.txt'  # 替换成你要保存的TXT文件路径

column_data = read_column_from_csv(csv_file_path, column_name)
result_string = write_column_data_to_string(column_data)
save_to_txt(txt_file_path, result_string)

print(f"数据已保存到 {txt_file_path}")
