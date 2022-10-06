from __future__ import annotations
from cProfile import label
import json
import glob
from unicodedata import category
import cv2 as cv
import os
from matplotlib.pyplot import cla

from numpy import searchsorted

class tococo(object):
    def __init__(self,jpg_paths,label_path,save_path):
        self.images = []
        self.categories = []
        self.annotations = []
        # 返回地址
        self.jpgpaths = jpg_paths
        self.save_path = save_path
        self.label_path = label_path
        # 設置類別
        self.class_ids= {'pos':1}
        self.class_id = 1
        self.coco = {}

    def npz_to_coco(self):
        annid = 0
        for num,jpg_path in enumerate(self.jpgpaths):

            imgname = jpg_path.split('\\')[-1].split('.')[0]
            img=cv.imread(jpg_path)
            jsonf = open(self.label_path+imgname+'.json').read()
            labels =json.loads(jsonf)
            h,w = img.shape[:-1]
            self.images.append(self.get_images(imgname,h,w,num))
            for label in labels:
                px,py,pw,ph = label['x'],label['y'],label['w'],label['h']
                box =[px,py,pw,ph]
                print(box)
                self.annotations.append(self.get_annotations(box,num,annid,label['class']))
                annid = annid+1
        self.coco['images'] = self.images
        self.categories.append(self.get_categories(label['class'],self.class_id))
        self.coco["categories"] = self.categories
        self.coco['annotations'] = self.annotations
    def get_images(self,filename,height,width,image_id):
        image ={}
        image["height"] = height
        image['width'] = width
        image["id"] = image_id
        
        image["file_name"] = filename+'.jpg'

        return image
    def get_categories(self,name,class_id):
        category ={}
        category["supercategory"] = "Positive Cell"

        category['id'] = class_id
        category['name'] = name
        return category
    
    def get_annotations(self,box,image_id,ann_id,calss_name):
        annotation = {}
        w,h=box[2],box[3]
        area = w*h
        annotation['segmentation'] = [[]]
        annotation['iscrowd']=0
        annotation['image_id'] = image_id
        annotation['bbox'] = box
        annotation['area'] = float(area)

        annotation['category_id']=self.class_ids[calss_name]

        annotation['id'] = ann_id
        return annotation
    
    def save_json(self):
        self.npz_to_coco()
        label_dic = self.coco

        instances_train = json.dump(label_dic)

        f = open(os.path.join(save_path+'\instances_val12017.json'),w)
        f.write(instances_train)
        f.close()
jpg_paths = glob.glob('C:/Users/User/Desktop/coco/val/*.jpg')
    