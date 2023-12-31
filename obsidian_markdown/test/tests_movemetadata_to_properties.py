import sys
from pathlib import Path


sys.path.append('./obsidian_markdown')
sys.path.append('./obsidian_markdown/loggers')

import move_metadata_to_properties

#Setup Logger
from loggers.PrintLogger import PrintLogger
Logger = PrintLogger()

PROPERTIES = """
---
aliases:
tags: src/youtubevideo,ToDo/Cook,
date:  2021-12-05
People: ["[[The Dissenter]]", "[[Louise Barrett]]"]
---"""
TEXT: str = """---
aliases:
tags: src/youtubevideo,ToDo/Cook,
date:  2021-12-05
People: [[The Dissenter]],[[Louise Barrett]]
---
# Louise Barrett, Baboon Societies, Ecology, Embodied Cognition, and Evolutionary Psychology
---
## Key notes
- The brain is the module, not parts of the brain themselves.
- Cognition arises through a dynamic interaction between an organism and it's environment.

## Random Mentions
#### Books:
- Joseph Henrich: Weird culture
- Matthew cobbs - the idea of the brain
- [[Addiction by design]]
---
### Meta info
- Creator: [[The Dissenter]], [[Louise Barrett]]
- Episode: 551
- Themes: [[Evolution]]
- Series:
- Field:
- Found through:
- Url: https://www.youtube.com/watch?v=W4vJVrYZBlA
- Date: 2021-12-05
"""


def main():
    test_add_property_to_properties()
    test_get_property_value()
    test_move_metadata_to_properties()
    test_add_property()
    test_string_starts_with()
    test_add_propeties_base_if_not_exists()
    test_debug_edit_file()
    test_stringify_list()
    test_listify_string()

def test_add_property_to_properties():
    Logger.info(' Testing add proprty to propreties')
    test_cases = {
        'empty_values':{
            'input': {
                'properties': PROPERTIES,
                'key': 'empty_values',
                'value': ''
                    },
                'output':  PROPERTIES,
                'error_message': 'Failed empty test value'
            },
        'one_two':{
            'input': {
                'properties': """---\n---""",
                'key': 'Counts',
                'value': ["[[One]]","[[Two]]"]
                    },
                'output':  """---
Counts: ["[[One]]", "[[Two]]"]\n---""",
                'error_message': 'Failed empty test value'
            },
        'adding item to long format list':{
            'input': {
                'properties': """---
aliases:
tags: src/youtubevideo
date:  2023-05-02
People: 
- "[[John Vervaeke]]"
- "[[Jonathan Pageau]]"
url: https://www.youtube.com/watch?v=T1nxiLARYAk
---""",
                'key': 'People',
                'value': ["Henk"]
                    },
                'output': """---
aliases:
tags: src/youtubevideo
date:  2023-05-02
People: ["Henk", "[[John Vervaeke]]", "[[Jonathan Pageau]]"]
url: https://www.youtube.com/watch?v=T1nxiLARYAk
---""",
                'error_message': 'Failed empty test value'
            },
        'existing_key':{
            'input': {
                'properties': PROPERTIES,
                'key': 'People',
                'value': ["Henk"]
                    },
                'output':  """
---
aliases:
tags: src/youtubevideo,ToDo/Cook,
date:  2021-12-05
People: ["Henk", "[[Louise Barrett]]", "[[The Dissenter]]"]
---""",
                'error_message': 'Failed existing test value'
            },
        }
    for test, parameters in test_cases.items():
        new_properties = move_metadata_to_properties.add_property_to_properties(properties = parameters['input']['properties'], 
                                                           key = parameters['input']['key'],
                                                           values = parameters['input']['value'])
        test_check(result = new_properties, base_value = parameters['output'], test = test)
        
    return

def test_get_property_value():
    Logger.info(' Testing get_property_value')
    result = move_metadata_to_properties.get_property_value(properties = PROPERTIES, key = 'People')
    test_check(result = result, base_value = '["[[The Dissenter]]", "[[Louise Barrett]]"]', test = "get Property value")
    return

def test_move_metadata_to_properties():
    new_text = move_metadata_to_properties.move_metadata_to_properties(text = TEXT, 
                                           key = 'People', 
                                           metadata_keys = ['Creator', 'People'], 
                                           removed_metadata_keys = ['People'])
    test_result = """---
aliases:
tags: src/youtubevideo,ToDo/Cook,
date:  2021-12-05
People: ["[[Louise Barrett]]", "[[The Dissenter]]"]
---
# Louise Barrett, Baboon Societies, Ecology, Embodied Cognition, and Evolutionary Psychology
---
## Key notes
- The brain is the module, not parts of the brain themselves.
- Cognition arises through a dynamic interaction between an organism and it's environment.

## Random Mentions
#### Books:
- Joseph Henrich: Weird culture
- Matthew cobbs - the idea of the brain
- [[Addiction by design]]
---
### Meta info
- Creator: [[The Dissenter]], [[Louise Barrett]]
- Episode: 551
- Themes: [[Evolution]]
- Series:
- Field:
- Found through:
- Url: https://www.youtube.com/watch?v=W4vJVrYZBlA
- Date: 2021-12-05
""" 
    test_check(result = new_text, base_value = test_result, test = 'move_metadata_to_properties')

def test_add_property():
    new_text = move_metadata_to_properties.add_property(text = TEXT, key = 'People', values = ["Henk","Hanny"])
    check_result = """---
aliases:
tags: src/youtubevideo,ToDo/Cook,
date:  2021-12-05
People: ["Hanny", "Henk", "[[Louise Barrett]]", "[[The Dissenter]]"]
---
# Louise Barrett, Baboon Societies, Ecology, Embodied Cognition, and Evolutionary Psychology
---
## Key notes
- The brain is the module, not parts of the brain themselves.
- Cognition arises through a dynamic interaction between an organism and it's environment.

## Random Mentions
#### Books:
- Joseph Henrich: Weird culture
- Matthew cobbs - the idea of the brain
- [[Addiction by design]]
---
### Meta info
- Creator: [[The Dissenter]], [[Louise Barrett]]
- Episode: 551
- Themes: [[Evolution]]
- Series:
- Field:
- Found through:
- Url: https://www.youtube.com/watch?v=W4vJVrYZBlA
- Date: 2021-12-05
"""
    test_check(result = new_text, base_value = check_result, test = 'Add property')

def test_debug_edit_file():
    file_path = "D:\\Documents\\Drive\\Obsidian\\Knowledge vault\\Videos episodes\\Louise Barrett, Baboon Societies, Ecology, Embodied Cognition, and Evolutionary Psychology.md"
    base_path = Path(__file__).parent
    test_result_path = (base_path /"results/Liouse Barret result.md").resolve()
    Logger.info('Created debug file: {test_result_path}')
    move_metadata_to_properties.edit_file(file_path = file_path, save_path = test_result_path)

def test_string_starts_with():
    tests = {
        '---': {
            'input': """---
    ---""",
            'output': True},
        "\\n---": {
            'input': """\n---
    ---""",
            'output': True},
    "  ---": {
            'input': """\n  ---
    ---""",
            'output': True},
        "\\n  ---": {
            'input': """\n  ---
    ---""",
            'output': True},
    " random text---": {
            'input': """ random text---
    ---""",
            'output': False},
    }
    for test, parameters in tests.items():
        result = move_metadata_to_properties.string_starts_with(text = parameters['input'], startswith = '---')
        test_check(result = result, base_value = parameters['output'], test = f'Starts with "{test}"')

def test_add_propeties_base_if_not_exists():
    tests = {
        '  ':{
            'input': '  ',
            'output': '---\n---\n  '
        },
        '\\n\\n  ':{
            'input': '\n\n  ',
            'output': '---\n---\n\n\n  '
        },
        '---  ':{
            'input': '---  ',
            'output': '---  '
        },
        '---\\n---':{
            'input': '---\n---',
            'output': '---\n---'
        },
        '---\\ntext\\n---\\n':{
            'input': '---\ntext\n---\n',
            'output': '---\ntext\n---\n'
        },
        '# Title and stuff  ':{
            'input': '# Title and stuff  ',
            'output': '---\n---\n# Title and stuff  '
        },
    }
    for test, parameters in tests.items():
        result = move_metadata_to_properties.add_propeties_base_if_not_exists(text = parameters['input'])
        test_check(result = result, base_value = parameters['output'], test = f'Add properties section starts with "{test}"')  

def test_check(result, base_value, test):
    if result != base_value:
        Logger.error(f"Test: {test} failed")
        Logger.debug(result)
    else:
        Logger.info(f'Test: {test} succeeded')

def test_stringify_list():
    tests = {
        '["one", "two"]':{
            'input':["one","two"],
            'output':'["one", "two"]'
        }
    }
    for test, parameters in tests.items():
        result = move_metadata_to_properties.stringify_list(text_list = parameters['input'])
        test_check(result = result, base_value = parameters['output'], test = f'Stringify list "{test}"')

def test_listify_string():
    tests = {
        'one, two':{
            'input': 'one, two',
            'output': ['one', 'two']
        },
        '[one, two]':{
            'input': '[one, two]',
            'output': ['one', 'two']
        },
        '["[[one]]", "[[two]]"]':{
            'input': '["[[one]]", "[[two]]"]',
            'output': ['[[one]]', '[[two]]']
        },
    }
    for test, parameters in tests.items():
        result = move_metadata_to_properties.listify_string(text_string = parameters['input'])
        test_check(result = result, base_value = parameters['output'], test = f'Listify string "{test}"')

if __name__ == '__main__':
    main()