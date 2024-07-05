# Detect_money_uk - Yolov8 - Detect objects

Model detect_money_uk for library [yolov8](https://github.com/ultralytics/ultralytics)

## Requirements

- python3
- yolov8

## Install

```sh
pip3 install -r requirements.txt
```

## Train

```sh
yolo task=detect \
mode=train \
model=yolov8s.pt \
data=data/data.yaml \
epochs=10 \
imgsz=640
```

## Detect

```sh
yolo task=detect \
mode=predict \
model=model/model.pt \
conf=0.25 \
source='examples/coins.jpg'
```

## Test model

```sh
python3 detect.py
```

## Convert segments to polygons (After LabelStudio)

```sh
python3 data_seg/segpoly.py
```

## Labels

| Label      | Description      |
| :--------- | :--------------- |
| bn_1       | 1 banknote       |
| bn_10      | 10 banknote      |
| bn_100     | 100 banknote     |
| bn_1000    | 1000 banknote    |
| bn_2       | 2 banknote       |
| bn_20      | 20 banknote      |
| bn_200     | 200 banknote     |
| bn_5       | 5 backnote       |
| bn_50      | 50 backnote      |
| bn_500     | 500 backnote     |
| coin_1     | 1 coin           |
| coin_10    | 10 coin          |
| coin_10_bn | 10 coin banknote |
| coin_1_bn  | 1 coin banknote  |
| coin_2     | 2 coin           |
| coin_25    | 25 coin          |
| coin_2_bn  | 2 coin banknote  |
| coin_5     | 5 coin           |
| coin_50    | 50 coin          |
| coin_5_bn  | 5 coin banknote  |

## Google Colab

```txt
yolov8.ipynb
```

# Thanks

- [Yolov8](https://github.com/ultralytics/ultralytics)
- [LabelStudio](https://github.com/HumanSignal/label-studio)

## Examples

![example1](https://github.com/GAURCODER/YOLO_OBJECT_DETECT/blob/master/examples/coins.jpg?raw=true)

![example2](https://github.com/GAURCODER/YOLO_OBJECT_DETECT/blob/master/examples/example1.jpg?raw=true)

![example3](https://github.com/GAURCODER/YOLO_OBJECT_DETECT/blob/master/examples/example2.jpg?raw=true)

![example4](https://github.com/GAURCODER/YOLO_OBJECT_DETECT/blob/master/examples/example3.png?raw=true)

![example5](https://github.com/GAURCODER/YOLO_OBJECT_DETECT/blob/master/examples/example4.png?raw=true)
