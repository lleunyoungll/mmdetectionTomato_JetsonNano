_base_ = './configs/mask_rcnn/mask_rcnn_r50_fpn_2x_coco.py'

model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=2),
        mask_head=dict(num_classes=2),
    ),
    backbone=dict(
        depth=101,
        init_cfg=dict(type='Pretrained',
                        checkpoint='torchvision://resnet101')
    ))

dataset_type = 'COCODataset'
classes = ( 'Plant',
            'Disease')

optimizer = dict(  # Config used to build optimizer, support all the optimizers in PyTorch whose arguments are also the same as those in PyTorch
    type='SGD',  # Type of optimizers, refer to https://github.com/open-mmlab/mmdetection/blob/master/mmdet/core/optimizer/default_constructor.py#L13 for more details
    lr=0.01,  # Learning rate of optimizers, see detail usages of the parameters in the documentation of PyTorch
    momentum=0.9,  # Momentum
    weight_decay=0.0001)  # Weight decay of SGD
lr_config = dict(  # Learning rate scheduler config used to register LrUpdater hook
    policy='step',  # The policy of scheduler, also support CosineAnnealing, Cyclic, etc. Refer to details of supported LrUpdater from https://github.com/open-mmlab/mmcv/blob/master/mmcv/runner/hooks/lr_updater.py#L9.
    warmup='linear',  # The warmup policy, also support `exp` and `constant`.
    warmup_iters=1000,  # The number of iterations for warmup
    warmup_ratio=
    0.001,  # The ratio of the starting learning rate used for warmup
    step=[8, 11])  # Steps to decay the learning rate

data = dict(
    samples_per_gpu=4,
    workers_per_gpu=1,
    train=dict(
        img_prefix='./Train/',
        classes=classes,
        ann_file='./Train/annotations.json',
        ),
    val=dict(
        img_prefix='./Validation/',
        classes=classes,
        ann_file='./Validation/annotations.json'),
    test=dict(
        img_prefix='./Test/',
        classes=classes,
        ann_file='./Test/annotations.json'))

work_dir = 'work_dir'
#load_from = 'work_dir/epoch_24.pth'
runner = dict(type='EpochBasedRunner', max_epochs=300)

#checkpoint_config

