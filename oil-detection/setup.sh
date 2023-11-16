#!/bin/bash

git clone https://github.com/ultralytics/yolov5  # clone
cd yolov5
pip install -r requirements.txt  # install
cd ..

curl -L "https://app.roboflow.com/ds/M2L1dXRjXh?key=8dopNlqTet" > roboflow.zip; unzip roboflow.zip; rm roboflow.zip
cp data.yaml yolov5/data/
