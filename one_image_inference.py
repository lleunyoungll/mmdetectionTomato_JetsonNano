# -*- coding: utf-8 -*-
import mmcv
import torch
import numpy as np
from PIL import Image
import os

# json 파일 생성을 위한 모듈 import
import cv2
import json

from mmdet.apis import init_detector
from mmdet.apis import inference_detector

import PIL.ImageDraw as ImageDraw
import PIL.Image as Image



def draw_text(img, text,
          font=cv2.FONT_HERSHEY_PLAIN,
          pos=(0, 0),
          font_scale=1,
          font_thickness=1,
          text_color=(0, 255, 0),
          text_color_bg=(0, 0, 0)
          ):

    x, y = pos
    text_size, _ = cv2.getTextSize(text, font, font_scale, font_thickness)
    text_w, text_h = text_size
    cv2.rectangle(img, pos, (x + text_w, y + text_h), text_color_bg, -1)
    cv2.putText(img, text, (x, y + text_h + font_scale - 1), font, font_scale, text_color, font_thickness)

    return text_size
# 8.26 inference 한 json 파일 저장 함수
def get_json(model, img_path, folderorfile,percentage = 0.0):
    img_path=img_path.replace('\\','/')
    classes = model.CLASSES
    result = inference_detector(model, img_path)
    if isinstance(result, tuple):
        bbox_result, segm_result = result
        if isinstance(segm_result, tuple):
            segm_result = segm_result[0]
    else:
        bbox_result, segm_result = result, None
    if folderorfile=='folder':
        image_path = img_path.split('.')[0]
        _count=img_path.count('/')
        onlyimgname=img_path.split('/')[_count]
    else:
        _count=img_path.count('/')
        onlyimgname=img_path.split('/')[_count]
    print(onlyimgname)
    bboxes = np.vstack(bbox_result)
    labels = [
            np.full(bbox.shape[0], i, dtype=np.int32)
            for i, bbox in enumerate(bbox_result)
        ]
    if segm_result is not None:
        segs = [segm for segm_list in segm_result for segm in segm_list]
    else:
        segs = None
    labels = np.concatenate(labels)
    img_arr = cv2.imread(img_path)
    if folderorfile=='folder':
        _count=img_path.count('/')
        imgname=img_path.split('/')[_count]
        imgname = imgname.split('.')[0]
    else:
        _count=img_path.count('/')
        imgname=img_path.split('/')[_count]
        imgname = imgname.split('.')[0]

    rows,cols,channel=img_arr.shape
    alpha = 0.94
    conto =  np.zeros((rows,cols,channel), np.uint8)
    label=""
    for i in range(len(bboxes)):
        if bboxes[i, -1] >percentage: #percentage 0.4대신 0.9
            label=(str(labels[i]))
            if segs[i] is not None:
                mask = segs[i]
                if classes[int(label)]=='tomato_r':
                    conto[mask == True] = (0,0,200)
                elif classes[int(label)]=='tomato_g':
                    conto[mask == True] = (255,0,255)

            cropPtX=int(bboxes[i,0])
            cropPtY=int(bboxes[i,1])
            cropW=int(bboxes[i,2]) - int(bboxes[i,0])
            cropH=int(bboxes[i,3]) - int(bboxes[i,1])

            res_probability=str(bboxes[i,-1])[:8]
            res_probability_f=float(res_probability)
            cv2.rectangle(img_arr, (cropPtX,cropPtY), (cropPtX+cropW,cropPtY+cropH), (0,0,255), thickness=None, lineType=None, shift=None)
            showrestext=classes[int(label)]+"|"+str(round(res_probability_f,4))
            pos=(cropPtX,cropPtY)
            draw_text(img_arr, showrestext, pos=pos)

    dlres = img_arr
    img_arr=cv2.addWeighted(img_arr, alpha, conto, (1-alpha), 3)

    if not os.path.exists('testresult'):
        os.mkdir('testresult')

    if folderorfile=='folder':
        img_path=imgname.replace('\\','/')
        cv2.imwrite('testresult/'+imgname+'~res.jpg',dlres)
     
    elif folderorfile=='file':
        #cv2.imshow("result",dlres)
        img_path=imgname.replace('\\','/')
        cv2.imwrite('testresult/'+imgname+'~res.jpg',dlres)
        #print(classes[int(label)])
    return 1
