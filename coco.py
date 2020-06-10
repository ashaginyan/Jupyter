from pycocotools.coco import COCO
import requests
import cv2

annfile_train = 'standart/annotations/instances_train2017.json'
print(annfile_train)

a = COCO(annfile_train)
catIds = a.getCatIds(catNms=['train'])


imgIds = a.getImgIds(catIds=[7])

imgId = imgIds[1]


imgs = a.loadImgs([imgId])

annId = a.getAnnIds(imgIds=[imgId])
ann = a.loadAnns(annId)
print(ann[1]['bbox'], imgs[0]['file_name'])
img_name = imgs[0]['file_name']
bbox = ann[1]['bbox']

