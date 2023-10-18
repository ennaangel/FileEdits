import sys
sys.path.append('./obsidian_markdown')

import move_metadata_to_properties

PROPERTIES = """
---
aliases:
tags: src/youtubevideo,ToDo/Cook,
date:  2021-12-05
People: [[The Dissenter]],[[Louise Barrett]]
---"""
TEXT: str = """
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
    errors = 0
    for test, parameters in test_cases.items():
        new_properties = move_metadata_to_properties.add_property_to_properties(properties = parameters['input']['properties'], 
                                                           key = parameters['input']['key'],
                                                           value = parameters['input']['value'])
        if new_properties != parameters['output']:
            print(f'[ERROR]{parameters["error_message"]}\n')
            print('\n-------------------')
            print(new_properties)
            print('-------------------\n')
            errors += 1
        else:
            print(f'[INFO] {test} passed')
    print(f"[INFO] Failed tests: {errors}\n")
    return

def test_get_property_value():
    print('[INFO] Testing get_property_value')
    assert move_metadata_to_properties.get_property_value(properties = PROPERTIES, key = 'People').strip() == '[[The Dissenter]],[[Louise Barrett]]'
    print('[INFO] get property value passed')
    return

if __name__ == '__main__':
    main()