import sys
from pathlib import Path

sys.path.append('./obsidian_markdown')

import move_metadata_to_properties

PROPERTIES = """
---
aliases:
tags: src/youtubevideo,ToDo/Cook,
date:  2021-12-05
People: [[The Dissenter]],[[Louise Barrett]]
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
    test_debug_edit_file()

def test_add_property_to_properties():
    print('[INFO] Testing add proprty to propreties')
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
        'existing_key':{
            'input': {
                'properties': PROPERTIES,
                'key': 'People',
                'value': 'Henk'
                    },
                'output':  """
---
aliases:
tags: src/youtubevideo,ToDo/Cook,
date:  2021-12-05
People: Henk,[[Louise Barrett]],[[The Dissenter]]
---""",
                'error_message': 'Failed existing test value'
            },
        }
    for test, parameters in test_cases.items():
        new_properties = move_metadata_to_properties.add_property_to_properties(properties = parameters['input']['properties'], 
                                                           key = parameters['input']['key'],
                                                           value = parameters['input']['value'])
        test_check(result = new_properties, base_value = parameters['output'], test = test)
        
    return

def test_get_property_value():
    print('[INFO] Testing get_property_value')
    assert move_metadata_to_properties.get_property_value(properties = PROPERTIES, key = 'People').strip() == '[[The Dissenter]],[[Louise Barrett]]'
    print('[INFO] get property value passed')
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
People: [[Louise Barrett]],[[The Dissenter]]
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
    new_text = move_metadata_to_properties.add_property(text = TEXT, key = 'People', value = 'Henk, Hanny')
    check_result = """---
aliases:
tags: src/youtubevideo,ToDo/Cook,
date:  2021-12-05
People: Hanny,Henk,[[Louise Barrett]],[[The Dissenter]]
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
    print(test_result_path)
    move_metadata_to_properties.edit_file(file_path = file_path, save_path = test_result_path)

def test_check(result, base_value, test):
    if result != base_value:
        print(f"[ERROR] {test} test failed")
        print("###################")
        print(result)
        print("###################")
    else:
        print(f'[INFO] {test} succeeded')

if __name__ == '__main__':
    main()