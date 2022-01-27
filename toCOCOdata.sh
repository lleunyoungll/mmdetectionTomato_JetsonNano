python labelme2coco.py imgjsonDataset Train --labels labels.txt
python labelme2coco.py imgjsonDataset Validation --labels labels.txt
python labelme2coco.py imgjsonDataset Test --labels labels.txt
echo "all datasets are converted to COCO format completely!"