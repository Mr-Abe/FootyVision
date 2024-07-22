from ultralytics import YOLO

model = YOLO('yolov8x')

results = model.predict('input_videos/C35bd9041_0 (1).mp4', save=True, stream=True)

print(results[0])

print('-----------------------------------------------------')

for box in results[0].boxes:
    print(box)