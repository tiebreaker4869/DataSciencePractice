#!/bin/bash

git clone https://github.com/ultralytics/yolov5  # clone
cd yolov5
pip install -r requirements.txt  # install
cd ..

wget https://box.nju.edu.cn/f/c07a22e992e543fcb081/?dl=1

unzip dataset.zip

rm dataset.zip

cp data.yaml yolov5/data/