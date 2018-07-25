from itertools import product
import argparse
import shutil
import json
import re
import os


def mkdir(root_dir: str, path: str):
    full_path: str = root_dir + path
    if not os.path.exists(full_path):
        os.mkdir(full_path)


def mkdirs(root_dir: str, dirs):
    for dir in dirs:
        mkdir(root_dir, dir)


def move(root_dir: str, filename: str, folder: str):
    return shutil.move(root_dir + filename, root_dir + folder)


def parse_args(args=None):
    parser = argparse.ArgumentParser(
        description='Filesort - a simple command line tool for sorting files'
    )
    parser.add_argument(
        'sort_to_folder',
        help='The name of the folder in the current'
             ' working directory to sort matching files into (if'
             ' the specified folder does not exist it will create one).'
    )
    parser.add_argument(
        'query', nargs='+',
        help='The query each filename will have to match'
             ' against in order to be sorted. Filesort will simply check'
             ' if a filename contains the query (case-insensitive).'
    )
    parser.add_argument(
        '--save', '--s',
        action='store_true',
        help='save sort config to presets'
    )
    parser.add_argument(
        '--use-presets', '--up',
        action='store_true',
        help='use specified presets'
    )
    parser.add_argument(
        '--regex', '--re',
        action='store_true',
        help='sort_by args will be used as regex queries'
    )
    return parser.parse_args(args)


def handle_presets(args):
    preset_path: str = os.path.dirname(os.path.realpath(__file__)) + '\\' + 'presets.json'

    if args.use_presets or args.save:
        if not os.path.exists(preset_path):
            with open(preset_path, 'w+') as f:
                f.write('{}')

    if args.use_presets:
        with open(preset_path, 'r') as f:
            schema: dict = {k: v for k, v in json.loads(f.read()).items() if k in args.query}
    else:
        schema: dict = {args.sort_to_folder: args.query}

    if args.save:
        with open(preset_path, 'r') as rf:
            presets: dict = json.loads(rf.read())
        with open(preset_path, 'w') as f:
            f.write(json.dumps({**presets, **schema}))

    return schema


def main(args=None):
    work_dir: str = os.getcwd() + '\\'
    args = parse_args(args)
    schema = handle_presets(args)
    files: list = os.listdir(work_dir)
    mkdirs(work_dir, schema.keys())

    for filename, (sort_to, queries) in product(files, schema.items()):
        for query in queries:
            if args.regex:
                match = re.match(query, filename)
            else:
                match = query.lower() in filename.lower()
            if match:
                move(work_dir, filename, sort_to)
                break


if __name__ == '__main__':
    main(input("Args: "))
