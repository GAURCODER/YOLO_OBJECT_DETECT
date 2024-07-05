import os
import cv2
import re
import json
import shutil
import uuid

mask_dir = './masks'
labels_dir = './labels'
raw_dir = './raw'
images_dir = './images'

labels = ['bn_1', 'bn_10', 'bn_100', 'bn_1000', 'bn_2', 'bn_20', 'bn_200', 'bn_5', 'bn_50', 'bn_500', 'coin_1', 'coin_10', 'coin_10_bn', 'coin_1_bn', 'coin_2', 'coin_25', 'coin_2_bn', 'coin_5', 'coin_50', 'coin_5_bn']

parse_data = []

shutil.rmtree(labels_dir)
os.mkdir(labels_dir)
shutil.rmtree(images_dir)
os.mkdir(images_dir)

print("############################")
print("Convert segments to polygons")
print("############################")

with open("data.json") as data:
    parse_data = json.load(data)

    for j in os.listdir(mask_dir):
        image_path = os.path.join(mask_dir, j)
        print(image_path)

        id_image = re.search(r"(?<=task\-)(\d+)", j)

        data_image = [el for el in parse_data if el['id'] == int(id_image.group(1))]
        
        unique_name = uuid.uuid4().hex
        name_image = unique_name + os.path.splitext(os.path.basename(data_image[0]['image']))[-1]
    
        raw_image = os.path.basename(data_image[0]['image'])
        label = labels.index(data_image[0]['tag'][0]['brushlabels'][0])

        mask = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        _, mask = cv2.threshold(mask, 1, 255, cv2.THRESH_BINARY)

        H, W = mask.shape
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        polygons = []
        for cnt in contours:
            if cv2.contourArea(cnt) > 200:
                polygon = []
                for point in cnt:
                    x, y = point[0]
                    polygon.append(x / W)
                    polygon.append(y / H)
                polygons.append(polygon)
     
        with open('{}.txt'.format(os.path.join(labels_dir, unique_name)), 'w') as f:
            for polygon in polygons:
                for p_, p in enumerate(polygon):
                    if p_ == len(polygon) - 1:
                        f.write('{}\n'.format(p))
                    elif p_ == 0:
                        f.write('{0} {1} '.format(label, p))
                    else:
                        f.write('{} '.format(p))

            f.close()


        shutil.copyfile(os.path.join(raw_dir, os.path.basename(data_image[0]['image'])), os.path.join(images_dir, name_image))


    data.close()

with open('data.yaml', 'w') as data:
    data.write("path: ../data\ntrain: images\nval: images\n\nnc: {0}\n\nnames: [{1}]".format(len(labels), ', '.join(labels)))

    data.close

print("############################")