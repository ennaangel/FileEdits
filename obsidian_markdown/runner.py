import os
from os.path import isfile, join

sys.path.append('./obsidian_markdown/config')

import configs
import move_metadata_to_properties


folder_path: str = configs.JsonConfigurator("obsidian_markdown/config/meta_to_props_config.json")

def get_file_list(path: str)-> list:
    all_items = os.listdir(path)
    only_files = [file for file in all_items if isfile(join(path, file))]
    only_md_files = [file for file in only_files if file.endswith(".md")]
    return only_md_files


def main():
    """"""
    files: list = get_file_list(folder_path)
    for file in files:
        print(file)
        full_path = join(folder_path, file)
        move_metadata_to_properties.edit_file(full_path)

if __name__ == "__main__":
    main()