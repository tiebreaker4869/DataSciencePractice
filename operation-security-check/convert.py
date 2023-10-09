import argparse
import os

# 把 yolo 的格式转换为 <class_id> <conf_score> <left> <top> <right> <bottom>
# 但是是百分比，而不是绝对坐标，要转换为绝对坐标需要再运行 conver_scale.py

def convert_files_in_folder(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):  # 仅处理.txt文件
            input_file = os.path.join(input_folder, filename)
            output_file = os.path.join(output_folder, filename)
            convert_yolo_to_custom_format(input_file, output_file)

def convert_yolo_to_custom_format(input_file, output_file):
    with open(input_file, "r") as f:
        lines = f.readlines()

    with open(output_file, "w") as f:
        for line in lines:
            line = line.strip().split()
            if len(line) >= 6:
                class_id = int(line[0])
                x, y, w, h, conf = map(float, line[1:])
                left = x - w / 2
                top = y - h / 2
                right = x + w / 2
                bottom = y + h / 2

                # 写入转换后的格式到输出文件
                f.write(f"{class_id} {conf} {left} {top} {right} {bottom}\n")

def main():
    parser = argparse.ArgumentParser(description="Batch convert YOLO format files to custom format")
    parser.add_argument("--input_folder", type=str, required=True, help="Input folder containing YOLO format files")
    parser.add_argument("--output_folder", type=str, required=True, help="Output folder for custom format files")
    args = parser.parse_args()

    os.makedirs(args.output_folder, exist_ok=True)
    convert_files_in_folder(args.input_folder, args.output_folder)

if __name__ == "__main__":
    main()
