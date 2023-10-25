import sys
from pathlib import Path

sys.path.append('./obsidian_markdown')
sys.path.append('./obsidian_markdown/loggers')

#Setup Logger
from loggers.PrintLogger import PrintLogger
Logger = PrintLogger()


sys.path.append('./obsidian_markdown/config')

import configs


def main():
    Configurations = test_create_configurator()
    test_attr_path(Configurations)
    test_get_value(Configurations)


def test_create_configurator():
    Configurations = configs.JsonConfigurator("obsidian_markdown/config/meta_to_props_config.json")
    return Configurations

def test_attr_path(Configurations):
    result = Configurations.path
    test_check(result, "obsidian_markdown/config/meta_to_props_config.json", 'path test') 

def test_get_value(Configurations):
    result = Configurations.get_value('folder')
    test_check(result, "D:\\Documents\\Drive\\Obsidian\\Knowledge vault\\Books", 'get folder value test')

def test_check(result, base_value, test):
    if result != base_value:
        Logger.error(f"Test: {test} failed")
        Logger.debug(result)
    else:
        Logger.info(f'Test: {test} succeeded')

if __name__ == '__main__':
    main()