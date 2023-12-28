from ultralytics import RTDETR

# Load a COCO-pretrained RT-DETR-l model
model = RTDETR('rtdetr-x.pt')
# model = RTDETR('runs/detect/train27/weights/best.pt')
# Display model information (optional)
model.info()

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data='data.yaml', epochs=2000, imgsz=1024, patience=300, optimizer='AdamW', lr0=5e-4, batch=8, cos_lr=True, rect=True)

result = model.val(imgsz=1024, rect=True)