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
        




def FolderDL(folder_selected):
        print(folder_selected)
        S.server_activate(folder_selected,'folder')
def fileDL(file_selected):
        print(file_selected)
        S.server_activate(file_selected,'file')

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
    parser = argparse.ArgumentParser(description='DataPath')
    parser.add_argument('--filepath', type=str, default="",
                    help='D drive data path')
    parser.add_argument('--folderpath', type=str, default="",
                    help='D drive data path')

    args = parser.parse_args()

    file_selected=args.filepath
    folder_selected=args.folderpath
    
    if file_selected!="":
        fileDL(file_selected)
    if folder_selected!="":
        FolderDL(folder_selected)
    

    
