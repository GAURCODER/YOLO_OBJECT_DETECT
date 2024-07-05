from ultralytics import YOLO
import cv2 as cv
import cvzone
import math
import re

model = YOLO("model/model.pt")
model.fuse()

classNames = ['bn_1', 'bn_10', 'bn_100', 'bn_1000', 'bn_2', 'bn_20', 'bn_200', 'bn_5', 'bn_50', 'bn_500', 'coin_1', 'coin_10', 'coin_10_bn', 'coin_1_bn', 'coin_2', 'coin_25', 'coin_2_bn', 'coin_5', 'coin_50', 'coin_5_bn']

img = "examples/coins.jpg"

image_read = cv.imread(img)

result = model(img)

coins = []

for result in result:
    boxes = result.boxes

    for box in boxes:
        x1, y1, x2, y2 = box.xyxy[0]
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

        w, h = x2 - x1, y2 - y1

        cvzone.cornerRect(image_read, (x1, y1, w, h), l=9)

        conf = math.ceil((box.conf[0] * 100) / 100)

        cls = int(box.cls[0])
        currentClass = classNames[cls]
        coins.append(classNames[cls])
            
        cvzone.putTextRect(image_read, f'{classNames[cls]} ({conf})', (max(0, x1), max(35, y1)), scale=0.6, thickness=1)
        


money = 0
amount = dict((i, coins.count(i)) for i in coins)

for key in amount:
    if key == 'coin_1' or key == 'bn_1': 
        money += (amount[key] * 1)
    elif key == 'coin_2':
        money += (amount[key] * 2)
    elif key == 'coin_5':
        money += (amount[key] * 5)
    elif key == 'coin_10' or key == 'bn_10':
        money += (amount[key] * 10)
    elif key == 'coin_25':
        money += (amount[key] * 25)
    elif key == 'coin_50' or key == 'bn_50':
        money += (amount[key] * 50)
    elif key == 'bn_20':
        money += amount[key] * 20
    elif key == 'bn_100':
        money += amount[key] * 100
    elif key == 'bn_200':
        money += amount[key] * 200
    elif key == 'bn_500':
        money += amount[key] * 500
    elif key == 'bn_1000':
        money += amount[key] * 1000
    elif key == 'coin_1_bn':
        money += (amount[key] * 1) * 100
    elif key == 'coin_2_bn':
        money += (amount[key] * 2) * 100
    elif key == 'coin_5_bn':
        money += (amount[key] * 5) * 100
    elif key == 'coin_10_bn':
        money += (amount[key] * 10) * 100

cvzone.putTextRect(image_read, f'Total: {money}', (1, 50))

cv.imshow("Image", image_read)
cv.waitKey(0) & 0xFF == ord('q')

cv.destroyAllWindows()