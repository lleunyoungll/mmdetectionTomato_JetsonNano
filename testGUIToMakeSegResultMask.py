import socket
from os import walk
import os
import time
from PIL import Image
import cv2
from torch.nn.functional import threshold
#Custom Function
from one_image_inference import get_json

from mmdet.apis import init_detector
from mmdet.apis import inference_detector
from mmcv import Config
import glob

from threading import Thread
import time
import os.path
import re
import pyparsing as pp
class Server:
    #global img_path_list_by_jpg
    def __init__(self,
                model_path:str='',
                threshold:int=0.0
                ):
        self.model_path = model_path
        self.threshold = threshold
        self.dataloader = None


    def load_model(self):
        # TODO
        """[모델의 가중치 및 하이퍼파라미터 값 로드]
        model initialize

        setting model pth
        """
        cfg = Config.fromfile("customized_config.py")
        self.model = init_detector(cfg, checkpoint=self.model_path)

        print(f'[server]default model AI Server is ready')

    def server_activate(self,selected,folderorfile):
        returnNum=-1
        if folderorfile=='folder':
            testResultDataset_dir = selected
            testResultDataset_filelist = os.listdir(testResultDataset_dir)
            for i in range(len(testResultDataset_filelist)):
                one_img_path=os.path.join(testResultDataset_dir,testResultDataset_filelist[i])
                returnNum=get_json(self.model,
                    one_img_path,
                    folderorfile,
                    percentage=self.threshold)
            os.startfile('testresult')
        elif folderorfile=='file':
            print("selected fileNm: "+selected)
            returnNum=get_json(self.model,
                    selected,
                    folderorfile,
                    percentage=self.threshold)
        return returnNum
        

from tkinter import *
from tkinter import filedialog

def quit():
    global win
    win.quit()

if __name__ =='__main__':
    global folder_selected
    global file_selected

    f=open('model_path.txt','r')
    model_path_fromfile=f.readline()
    f.close()
    S = Server(
            model_path=os.path.join(model_path_fromfile),
            threshold = 0.6
            )
    S.load_model()
    win=Tk() #창 생성
    win.geometry("500x200")
    win.title("[PlantCare]식물상태 판독 프로그램")
    win.option_add("*Font","맑은고딕 10")
    '''
    label=Label(win,text='')
    label.pack()
    '''
    btn=Button(win)
    btn2=Button(win)
    btn.config(width=20,height=5)
    btn2=Button(width=20,height=5)
    
    btn.config(text="폴더 선택하기")
    btn2.config(text="파일 선택하기")

    btn3=Button(win,text="Quit",command=quit).pack()

    folder_selected=""
    file_selected=""
    returnNum=-1
    def FolderDL():
        global folder_selected
        folder_selected = filedialog.askdirectory()
        print(folder_selected)
        returnNum=S.server_activate(folder_selected,'folder')
    def fileDL():
        global file_selected
        file_selected = filedialog.askopenfilename()
        print(file_selected)
        returnNum=S.server_activate(file_selected,'file')

    btn.config(command=FolderDL)
    btn.pack(side="left",padx=50)
    btn2.config(command=fileDL)
    btn2.pack(side="left",padx=20)

    win.mainloop() #창 실행
    #if returnNum==1:  #작업 끝났으면 창 닫기
    #    win.quit()
