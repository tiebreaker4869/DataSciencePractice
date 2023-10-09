#!/bin/bash

cd yolov5
python train.py --img 640 --epoch 100 --data data.yaml --weights yolov5s.pt
cd ..