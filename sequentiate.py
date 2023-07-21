"""
This script functions to grab a bunch of images paired with their masks and add
them to OURS dataset, in order to keep internal consistency, and order.
"""
import argparse
import utils
import pandas as pd
from pathlib import Path
import shutil


def arg_parse():
    parser = argparse.ArgumentParser()

    parser.add_argument('-i', '--input', dest='input_path', type=str,
                        required=True,
                        help='Path to the source images folder.')
    parser.add_argument('-m', '--mask', dest='mask_path', type=str,
                        required=True, help='Path to the masks folder.')
    parser.add_argument('-o', '--output', dest='output_path', type=str,
                        required=True,
                        help='Path to the destiny images folder.')
    parser.add_argument('--csv', type=str, required=True,
                        help='Path to the .csv file.')

    parser.add_argument('--hour', type=int)
    parser.add_argument('--culture', type=str)
    parser.add_argument('--lens', type=int)
    parser.add_argument('--scientist', type=str)
    parser.add_argument('--date', type=str)
    parser.add_argument('--difficulty', type=str)

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


def try_load_csv(path):

    try:
        return pd.read_csv(path)
    except:
        return None


def func():
    '''
    Receives a path, grabs all the images in that path, grabs all the masks.
    Checks the highest idx in the CSV, starts from there. Moves the grabbed
    images to OURS folder, along side with their masks, following the hightest
    idx. Updates these entries to the CSV file, with their metadata
    '''
    pass


def main():
    args = arg_parse()

    check_out_folders(args.output_path)

    csv = try_load_csv(args.csv)

    csv_dict = {}
    csv_column_lst = ['file', 'hour', 'culture', 'lens', 'well', 'scientist', 'date', 'difficulty']
    for column in csv_column_lst:
        csv_dict[column] = []

    csv_start_idx = -1
    if csv is not None:
        csv_start_idx = csv.shape[0]
    else:
        csv_start_idx = 0

    images = Path(args.input_path).glob('./*')
    images = [x for x in sorted(images) if x.is_file()]

    idx = csv_start_idx
    for image in images:
        new_path = Path(args.output_path) / 'images' / f'{idx:04d}.png'
        csv_dict['file'].append(new_path.name)

        csv_dict['hour'].append(args.hour)
        csv_dict['culture'].append(args.culture)
        csv_dict['lens'].append(args.lens)
        csv_dict['well'].append(image.name[:-4])
        csv_dict['scientist'].append(args.scientist)
        csv_dict['date'].append(args.date)
        csv_dict['difficulty'].append(args.difficulty)

        # csv_file_lst.append(new_path.name)
        # image.replace(new_path)
        shutil.copy(image.resolve(), new_path.resolve())

        idx += 1

    masks = Path(args.mask_path).glob('./*')
    masks = [x for x in sorted(masks) if x.is_file()]

    idx = csv_start_idx
    for mask in masks:
        new_path = Path(args.output_path) / 'masks' / '0' / f'{idx:04d}.png'
        # mask.replace(new_path)
        shutil.copy(mask.resolve(), new_path.resolve())

        idx += 1

    print(f"file {len(csv_dict['file'])} \
            \nhour {len(csv_dict['hour'])} \
            \nculture {len(csv_dict['culture'])} \
            \nlens {len(csv_dict['lens'])} \
            \nwell {len(csv_dict['well'])} \
            \nscientist {len(csv_dict['scientist'])} \
            \ndate {len(csv_dict['date'])} \
            \ndifficulty {len(csv_dict['difficulty'])}")

    # df = pd.DataFrame(csv_file_lst, columns=csv_column_lst)
    df = pd.DataFrame(csv_dict)
    if csv is not None:
        print("MERGED")
        df = csv.append(df, ignore_index=True)
        # df = df.append(csv, ignore_index=True)
    df.to_csv(args.csv, index_label=False)


main()
