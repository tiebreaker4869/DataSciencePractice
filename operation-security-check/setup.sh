#!/bin/bash

git clone https://github.com/ultralytics/yolov5  # clone
cd yolov5
pip install -r requirements.txt  # install
cd ..

wget https://box.nju.edu.cn/f/2624b1ab1df948fbbd0a/?dl=1

unzip dataset.zip

rm dataset.zip

cp data.yaml yolov5/data/