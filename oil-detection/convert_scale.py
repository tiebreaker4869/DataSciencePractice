import argparse
import os
import cv2

def convert(input_folder, txt_folder, final_result):
    for filename in os.listdir(txt_folder):
        if filename.endswith(".txt"):
            txt_file = os.path.join(txt_folder, filename)
            image_file = os.path.join(input_folder, os.path.splitext(filename)[0] + ".jpg")
            final_txt_file = os.path.join(final_result, filename)
            final_lines = ''

            if os.path.exists(image_file):
                img = cv2.imread(image_file)
                img_height, img_width = img.shape[:2]
                with open(txt_file, "r") as f:
                    lines = f.readlines()

                for line in lines:
                    class_id, confidence, left, top, right, bottom = map(float, line.strip().split())
                    assert class_id == 0
                    confidence_str = f"{confidence:.2f}"

                    # 将百分比坐标转换为像素坐标
                    left = int(left* img_width)
                    top = int(top * img_height)
                    right = int(right * img_width)
                    bottom = int(bottom * img_height)
                    
                    final_lines = final_lines + 'oil' + ' ' + confidence_str + ' ' + str(left) + ' ' + str(top) + ' ' + str(right) + ' ' + str(bottom) + '\n'
                with open(final_txt_file, "w") as f:
                    f.write(final_lines)


def main():
    parser = argparse.ArgumentParser(description="Draw bounding boxes on images from YOLO format txt files")
    parser.add_argument("--input_folder", type=str, required=True, help="Input folder containing images")
    parser.add_argument("--txt_folder", type=str, required=True, help="Folder containing unscaled format txt files")
    parser.add_argument("--final_result", type=str, required=True, help="Output folder for final result txt.")
    args = parser.parse_args()

    os.makedirs(args.final_result, exist_ok=True)
    convert(args.input_folder, args.txt_folder, args.final_result)

if __name__ == "__main__":
    main()
