#!/bin/bash

git clone https://github.com/ultralytics/yolov5  # clone
cd yolov5
pip install -r requirements.txt  # install
cd ..

wget -O dataset.zip https://box.nju.edu.cn/f/78d7fda5b1204daf8aa2/?dl=1

unzip dataset.zip

rm dataset.zip

cp data.yaml yolov5/data/