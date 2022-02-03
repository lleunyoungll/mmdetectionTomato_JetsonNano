- **Compact MMDetection For Tomato Detect in Jetson Nano Board**

## Introduction

image detection & segmentation for tomato using mmdetection library (mmdetection original: https://github.com/open-mmlab/mmdetection )



## Installation

- **Miniforge(conda) Must Be Prepared**
- **Conda Environment Prepare**
- ```git clone https://github.com/lleunyoungll/mmdetectionTomato_JetsonNano.git```
- ```cd mmdetectionTomato_JetsonNano ```
- ```conda env create --file mmdet369.yaml```



## Test

- first, prepare model weight in "link" here -> https://drive.google.com/file/d/1Xo-Xk7gN6RBcBHEYGLq_3ZFkQcqPLNSP/view?usp=sharing
- copy above downloaded model weight file and paste into 'savedModel' directory
- then, modify 'saved_model.txt' contents to copied model file name
- ```python testGUIToMakeSegResultMask.py```
- result images will be in 'testresult/' folder



## Custom Dataset

- If you want to train for your own dataset. Make labeling data using below annotation tool(Labelme.exe)
    https://drive.google.com/file/d/16meD3s6r9VsrRfSsUmlaSMnGDiAZ_Sve/view?usp=sharing
- make labeling like this below ↓

  ![labeling](https://user-images.githubusercontent.com/98143576/152295166-4c6797c1-36e3-488a-9ca7-b46204abbce2.gif)
- If you do labeling, you have image files and json files
- Delete all files in 'imgjsonDataset_8timeSmallSize' directory, then Put above your image and json files you made in Labelme.exe into 'imgjsonDataset_8timeSmallSize' directory


## Train

- open a terminal & conda and activate mmdet359 environment
- ```cd mmdetectionTomato_JetsonNano```
- ```./toCOCOdata_8timeSmallSize.sh```
- then 'Train', 'Test', 'Validation' 3 folders will be made in that directory(mmdetectionTomato_JetsonNano)
- ```python tools/train.py customized_config.py```
- then epoch files will be put in 'work_dir' directory


## Benchmark and model zoo

Results and models are available in the [model zoo](docs/model_zoo.md).

Supported backbones:

- [x] ResNet (CVPR'2016)

Supported methods:

- [x] [Mask R-CNN (ICCV'2017)](configs/mask_rcnn)
- [x] [GCNet (ICCVW'2019)](configs/gcnet/README.md)
- [x] [DetectoRS (ArXiv'2020)](configs/detectors/README.md)
- [x] [YOLACT (ICCV'2019)](configs/yolact/README.md)

Some other methods are also supported in [projects using MMDetection](./docs/projects.md).



## Citation

If you use this toolbox or benchmark in your research, please cite this project.

```
@article{mmdetection,
  title   = {{MMDetection}: Open MMLab Detection Toolbox and Benchmark},
  author  = {Chen, Kai and Wang, Jiaqi and Pang, Jiangmiao and Cao, Yuhang and
             Xiong, Yu and Li, Xiaoxiao and Sun, Shuyang and Feng, Wansen and
             Liu, Ziwei and Xu, Jiarui and Zhang, Zheng and Cheng, Dazhi and
             Zhu, Chenchen and Cheng, Tianheng and Zhao, Qijie and Li, Buyu and
             Lu, Xin and Zhu, Rui and Wu, Yue and Dai, Jifeng and Wang, Jingdong
             and Shi, Jianping and Ouyang, Wanli and Loy, Chen Change and Lin, Dahua},
  journal= {arXiv preprint arXiv:1906.07155},
  year={2019}
}
```



## Projects in OpenMMLab

- [MMCV](https://github.com/open-mmlab/mmcv): OpenMMLab foundational library for computer vision.
- [MIM](https://github.com/open-mmlab/mim): MIM Installs OpenMMLab Packages.
- [MMClassification](https://github.com/open-mmlab/mmclassification): OpenMMLab image classification toolbox and benchmark.
- [MMDetection](https://github.com/open-mmlab/mmdetection): OpenMMLab detection toolbox and benchmark.
- [MMDetection3D](https://github.com/open-mmlab/mmdetection3d): OpenMMLab's next-generation platform for general 3D object detection.
- [MMSegmentation](https://github.com/open-mmlab/mmsegmentation): OpenMMLab semantic segmentation toolbox and benchmark.
- [MMAction2](https://github.com/open-mmlab/mmaction2): OpenMMLab's next-generation action understanding toolbox and benchmark.
- [MMTracking](https://github.com/open-mmlab/mmtracking): OpenMMLab video perception toolbox and benchmark.
- [MMPose](https://github.com/open-mmlab/mmpose): OpenMMLab pose estimation toolbox and benchmark.
- [MMEditing](https://github.com/open-mmlab/mmediting): OpenMMLab image and video editing toolbox.
- [MMOCR](https://github.com/open-mmlab/mmocr): A Comprehensive Toolbox for Text Detection, Recognition and Understanding.
- [MMGeneration](https://github.com/open-mmlab/mmgeneration): OpenMMLab image and video generative models toolbox.
