python labelme2coco.py imgjsonDataset_8timeSmallSize Train --labels labels.txt
python labelme2coco.py imgjsonDataset_8timeSmallSize Validation --labels labels.txt
python labelme2coco.py imgjsonDataset_8timeSmallSize Test --labels labels.txt
echo "all datasets are converted to COCO format completely!"