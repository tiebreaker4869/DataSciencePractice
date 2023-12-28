#!/bin/bash

pip install ultralytics

wget -O dataset.zip https://box.nju.edu.cn/f/78d7fda5b1204daf8aa2/?dl=1

mkdir datasets

cd datasets

mkdir operation-security-check

cp ../dataset.zip operation-security-check/

cd operation-security-check

unzip dataset.zip

rm dataset.zip

cd ../..

rm dataset.zip

cp datasets/operation-security-check/data.yaml data.yaml