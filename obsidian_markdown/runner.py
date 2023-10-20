import os
from os.path import isfile, join

import move_metadata_to_properties

folder_path: str = 'D:\\Documents\\Drive\\Obsidian\\Knowledge vault\\Videos episodes'

def get_file_list(path: str)-> list:
    all_items = os.listdir(path)
    only_files = [file for file in all_items if isfile(join(path, file))]
    return only_files


def main():
    """"""
    files: list = get_file_list(folder_path)
    for file in files:
        full_path = join(folder_path, file)
        move_metadata_to_properties.edit_file(full_path)

if __name__ == "__main__":
    main()