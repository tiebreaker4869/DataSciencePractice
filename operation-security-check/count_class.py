import os
import argparse
from collections import defaultdict

# 设置命令行参数解析
parser = argparse.ArgumentParser(description='统计YOLO格式标签文件中的各个类别数量')
parser.add_argument('label_dir', type=str, help='标签文件所在的目录')

# 解析命令行参数
args = parser.parse_args()

# 创建一个默认字典来存储类别计数
class_counts = defaultdict(int)

# 获取命令行输入的目录路径
label_files_directory = args.label_dir

# 检查目录是否存在
if not os.path.exists(label_files_directory):
    print(f"错误：目录 {label_files_directory} 不存在。")
    exit()

# 遍历目录中的所有标签文件
for label_file_name in os.listdir(label_files_directory):
    # 确保是文件而且具有.txt扩展名
    if label_file_name.endswith('.txt'):
        # 构建完整的文件路径
        file_path = os.path.join(label_files_directory, label_file_name)
        
        # 打开文件并逐行读取
        with open(file_path, 'r') as file:
            for line in file:
                # 分割行以获取类别ID
                class_id = line.split()[0]
                # 对该类别计数
                class_counts[class_id] += 1

# 打印类别计数结果
for class_id, count in sorted(class_counts.items()):
    print(f"Class ID {class_id}: {count}")