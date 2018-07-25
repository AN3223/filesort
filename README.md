# Filesort
A simple command line tool for sorting files, written in Python. Filesort will sort files in the current working directory into a specified folder based on filenames.

## Installation
`pip install filesort`

It installs straight to your Python "Scripts" directory, so just make sure that's in your PATH, then you're set to use Filesort.

## Usage
```
usage: filesort.py [-h] [--save] [--use-presets] [--regex]
                   sort_to_folder query [query ...]

Filesort - a simple command line tool for sorting files

positional arguments:
  sort_to_folder       The name of the folder in the current working directory
                       to sort matching files into (if the specified folder
                       does not exist it will create one).
  query                The query each filename will have to match against in
                       order to be sorted. Filesort will simply check if a
                       filename contains the query (case-insensitive).

optional arguments:
  -h, --help           show this help message and exit
  --save, --s          save sort config to presets
  --use-presets, --up  use specified presets
  --regex, --re        sort_by args will be used as regex queries
```

## Requirements
Python 3.5 or greater
