"""
This script functions to grab a bunch of images paired with their masks and add
them to OURS dataset, in order to keep internal consistency, and order.
"""
import argparse
import utils


def arg_parse():
    parser = argparse.ArgumentParser()

    parser.add_argument('-i', '--input', dest='input_path', type=str,
                        required=True, help='Path to the source images folder.')
    parser.add_argument('-o', '--output', dest='output_path', type=str,
                        required=True, help='Path to the destiny images folder.')
    parser.add_argument('--csv', type=str, required=True,
                        help='Path to the .csv file.')

    return parser.parse_args()


'''
Receives a path, grabs all the images in that path, grabs all the masks. Checks the highest idx in the CSV, starts from there. Moves the grabbed images to OURS folder, along side with their masks, following the hightest idx. Updates these entries to the CSV file, with their metadata
'''
def func():
    pass


def main():
    args = arg_parse()

    csv = utils.open_csv(args.csv)

    if not csv:
        idx = 0
    else:
        idx = len(csv)

    print(type(csv), idx)

    for idx, row in enumerate(csv):
        print(idx, row)


main()
