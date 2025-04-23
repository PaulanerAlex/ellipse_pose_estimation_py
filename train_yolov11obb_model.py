from ultralytics import YOLO

# Load a pretrained model
model = YOLO("yolo11s-obb.pt")

if __name__ == "__main__":
    # Train the model
    results = model.train(data="dataset/ellipse_recognition/ellipse_recognition.yml", epochs=250, imgsz=640)

# model = YOLO("runs/obb/train/weights/best.pt") # Load the trained model

# results = model("test4.jpg", show=True) # predict sample image

# # Access the results
# for result in results:
#     xywhr = result.keypoints.xy  # center-x, center-y, width, height, angle (radians)
#     xyxyxyxy = result.obb.xyxyxyxy  # polygon format with 4-points
#     names = [result.names[cls.item()] for cls in result.obb.cls.int()]  # class name of each box
#     confs = result.obb.conf  # confidence score of each box

