python ~/workspace/learning/utils/convertion/cv_convert.py --input ~/Downloads/48/ds0/img/ --output ~/Downloads/48/ds0/images/

FOLDER=~/Downloads/48/ds0/masks/

for file in "$FOLDER"/*; do
    echo $file
    python ~/workspace/learning/utils/dataset/normalize.py --input $file
done

python ~/workspace/learning/utils/dataset/rename_bulk.py --input ~/Downloads/48/ds0/images/ --pattern .tif
python ~/workspace/learning/utils/dataset/rename_bulk.py --input ~/Downloads/48/ds0/masks/ --pattern .tif

python sequentiate.py -i ~/Downloads/48/ds0/images/ -m ~/Downloads/48/ds0/masks/ -o ~/workspace/deep_learning/datasets/segmentation/ours/ --csv ~/workspace/deep_learning/datasets/segmentation/ours/ours.csv
