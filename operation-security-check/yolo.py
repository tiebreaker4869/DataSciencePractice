from ultralytics import YOLO

# Load a pretrained YOLO model (recommended for training)
model = YOLO('yolov8x.pt')

# Train the model using the 'coco128.yaml' dataset for 3 epochs
results = model.train(data='data.yaml', epochs=2000, patience=300, batch=8, scale=0.7, imgsz=1024, rect=True)


# Evaluate the model's performance on the validation set
results = model.val()