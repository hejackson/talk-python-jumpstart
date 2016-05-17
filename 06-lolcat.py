#!/usr/local/bin/python3

import os
import cat_service
import subprocess
import platform


def main():
    print_header()
    folder = get_or_create_output_folder()
    download_cats(folder)
    display_cats(folder)


def print_header():
    print('------------------------------')
    print('      CAT FACTORY')
    print('------------------------------')


def get_or_create_output_folder():
    folder = 'cat_pictures'
    print('__file__: ->{}<-'.format(__file__))
    base_folder = os.path.dirname(__file__)
    # full_path = os.path.abspath(os.path.join('.', folder))
    full_path = os.path.join(base_folder, folder)
    print(full_path)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('creating new dir at {}'.format(full_path))
        os.mkdir(full_path)

    return full_path


def download_cats(folder):
    print('contacting server to download cats...')
    cat_count = 8
    for i in range(1, cat_count + 1):
        name = 'lolcat_{}'.format(i)
        print('Downloading cat ' + name)
        cat_service.get_cat(folder, name)


def display_cats(folder):
    # open folder (OSX)
    print('Displaying cats in OS window...')
    if platform.system() == 'Darwin':
        subprocess.call(['open', folder])
    elif platform.system() == 'Windows':
        subprocess.call(['explorer', folder])
    elif platform.system() == 'Linux':
        subprocess.call(['xdg-open', folder])
    else:
        print("We don't support your os: " + platform.system())


if __name__ == '__main__':
    main()
