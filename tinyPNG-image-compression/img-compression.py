#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import tinify

tinify.key = 'your key'


def img_compression(filename, path):
    try:
        print('process ' + os.path.join(path, filename))
        source = tinify.from_file(os.path.join(path, filename))
        os.remove(os.path.join(path, filename))
        source.to_file(os.path.join(path, filename))
        print(os.path.join(path, filename) + ' done')
    except Exception as e:
        print(e)


def recursive_search_img(path):

    all_files = os.listdir(path)
    for file in all_files:
        if file != '.DS_Store' and os.path.isdir(os.path.join(path, file)):
            recursive_search_img(os.path.join(path, file))
        elif (file.endswith('.jpg') or file.endswith('.png') or file.endswith('.jpeg')):
            img_compression(file, path)


if __name__ == '__main__':
    recursive_search_img(sys.argv[1])
