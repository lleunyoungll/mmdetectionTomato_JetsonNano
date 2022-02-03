python labelme2coco.py imgjsonDataset_originalSize Train --labels labels.txt
python labelme2coco.py imgjsonDataset_originalSize Validation --labels labels.txt
python labelme2coco.py imgjsonDataset_originalSize Test --labels labels.txt
echo "all datasets are converted to COCO format completely!"