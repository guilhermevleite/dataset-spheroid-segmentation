"""
This script functions to grab a bunch of images paired with their masks and add
them to OURS dataset, in order to keep internal consistency, and order.
"""
import argparse
import utils
import pandas as pd
from pathlib import Path


def arg_parse():
    parser = argparse.ArgumentParser()

    parser.add_argument('-i', '--input', dest='input_path', type=str,
                        required=True, help='Path to the source images folder.')
    parser.add_argument('-m', '--mask', dest='mask_path', type=str,
                        required=True, help='Path to the masks folder.')
    parser.add_argument('-o', '--output', dest='output_path', type=str,
                        required=True, help='Path to the destiny images folder.')
    parser.add_argument('--csv', type=str, required=True,
                        help='Path to the .csv file.')

    return parser.parse_args()


def check_out_folders(path):
    '''
    Calls the function to create the adequate output folders and subfolders.

    TODO Update the msk path if this script ever works with multiple classes
    '''
    img = Path(path) / 'images'
    msk = Path(path) / 'masks' / '0'

    utils.create_dir(img)
    utils.create_dir(msk)


def func():
    '''
    Receives a path, grabs all the images in that path, grabs all the masks. Checks the highest idx in the CSV, starts from there. Moves the grabbed images to OURS folder, along side with their masks, following the hightest idx. Updates these entries to the CSV file, with their metadata
    '''
    pass


def main():
    args = arg_parse()

    check_out_folders(args.output_path)

    images = Path(args.input_path).glob('./*')
    images = [x for x in sorted(images) if x.is_file()]

    # CSV variables, by column name
    csv_file_lst = []
    csv_column_lst = ['file']

    for idx, image in enumerate(images):
        new_path = Path(args.output_path) / 'images' / '{}.png'.format(idx)
        csv_file_lst.append(new_path.name)
        image.replace(new_path)

    masks = Path(args.mask_path).glob('./*')
    masks = [x for x in sorted(masks) if x.is_file()]

    for idx, mask in enumerate(masks):
        new_path = Path(args.output_path) / 'masks' / '0' / '{}.png'.format(idx)
        mask.replace(new_path)

    df = pd.DataFrame(csv_file_lst, columns=csv_column_lst)
    df.to_csv(args.csv)

main()
