import re

folder_path: str = 'D:\\Documents\\Drive\\Obsidian\\Knowledge vault\\Videos episodes'
file_name: str = 'Louise Barrett, Baboon Societies, Ecology, Embodied Cognition, and Evolutionary Psychology.md'

def edit_file(file_path: str, save_path = None):
    with open(file_path, encoding='utf-8') as f:
        text: str = f.read()
        text = add_propeties_base_if_not_exists(text = text)
        text = move_metadata_to_properties(text = text, 
                                           key = 'People', 
                                           metadata_keys = ['Creator', 'People', 'people', 'Writer'], 
                                           removed_metadata_keys = ['People', 'people'])
        text = move_metadata_to_properties(text = text, 
                                           key = 'url', 
                                           metadata_keys = ['Url', 'url'], 
                                           removed_metadata_keys = ['Url', 'url'])
        text = move_metadata_to_properties(text = text, 
                                           key = 'themes', 
                                           metadata_keys = ['Themes', 'themes'], 
                                           removed_metadata_keys = ['Themes', 'themes'])
    if save_path == None:
        save_path = file_path
    with open(save_path, 'w', encoding='utf-8') as f:
        f.write(text)

def move_metadata_to_properties(text: str, key: str, metadata_keys: list, removed_metadata_keys: list):
    property_value = get_values_as_list(text = text, metadata_keys = metadata_keys)
    new_text = add_property(text = text, key = key, values = property_value)
    for metadata_key in removed_metadata_keys:
        new_text = remove_metadata(text = new_text, key = metadata_key)
    return new_text

def add_propeties_base_if_not_exists(text: str):
    if string_starts_with(text = text, startswith = '---'):
        return text
    new_text = re.sub("\A", "---\n---\n", text)
    return new_text

def string_starts_with(text: str, startswith: str):
    """Returns True if string starts with --- and any blanks and line breaks before it."""
    return re.search(f'\A(\s*|\n*){startswith}', text) != None

def add_property(text: str, key: str, values: list):
    properties = get_properties(text)
    new_properties = add_property_to_properties(properties = properties, key = key, values = values)
    text = text.replace(properties, new_properties)
    return text
    
def get_values_as_string(text: str, metadata_keys: list):
    values = []
    for key in metadata_keys:
        value = get_metadata(text = text, key = key)
        value = listify_string(text_string = value)
        values = values + value
    values = ','.join(values)
    return values

def get_values_as_list(text: str, metadata_keys: list)-> list:
    values = []
    for key in metadata_keys:
        value = get_metadata(text = text, key = key)
        value = listify_string(text_string = value)
        values = values + value
    return values

def add_property_to_properties(properties: str, key: str, values: list):
    """Add a new property to the old properties as a key value pair"""
    if values == '' or []:
        return properties
    if re.search(f'{key}:', properties) != None:
        return append_property_value_to_properties(properties, key, values)
    return add_new_property_to_properties(properties, key, values)

def add_new_property_to_properties(properties, key, value):
    """Adds a new propertie to proprties"""
    new_property = key+': '+ stringify_list(text_list = value)
    properties = re.sub('\n---', repl = f'\n{new_property}\n---', string = properties)
    return properties

def append_property_value_to_properties(properties, key, value):
    """Appens the new values to the already exisitn proprties"""
    cur_values = get_property_value(properties, key)
    cur_values = listify_property(cur_values)
    all_values = sorted(list(set(cur_values + value)))
    all_values = stringify_list(text_list = all_values)
    new_property = f'{key}: {all_values}\n'
    properties = re.sub(f'{key}:(.|\n- )*\n', new_property, properties)
    return properties

def get_metadata(text:str, key: str)-> str:
    """Returns the value for the given"""
    metadata = re.search(f'(?<=- {key}: )(.*)(?=\n)', text)
    if metadata == None:
        return ''
    return metadata.group()

def remove_metadata(text: str, key: str)->str:
    return re.sub(f'- {key}: (.*)\n', '', text)

def get_properties(text: str)-> str:
    properties = re.search('---((\n|.)*?)---', text)
    if properties == None:
        return ''
    return properties.group()

def get_property_value(properties: str, key: str)-> str:
    value = re.search(f'(?<={key}:)(.|\n- )*', properties).group()
    value = value.strip()
    return value

def listify_property(text_string: str):
    text_string = text_string.replace('\n- ',',')
    text_string = text_string.replace('- ',',')
    list_text = listify_string(text_string = text_string, sep = ',')
    return list_text

def listify_string(text_string: str, sep: str = ','):
    if text_string == '':
        return []
    text_string = re.sub('(?<!\[)\[(?!\[)','',text_string) #Remove single apperaneces of [
    text_string = re.sub('(?<!\])\](?!\])','',text_string) #Remove single apperaneces of ]
    list_text: list = text_string.split(sep)
    list_text = [words.strip() for words in list_text]
    list_text = [words.replace('"', '') for words in list_text]
    list_text = [words for words in list_text if words != '']
    return list_text

def stringify_list(text_list: list)-> str:
    text_string = str(text_list)
    text_string = text_string.replace("'", '"')
    return text_string

if __name__ == '__main__':
    file_path: str = folder_path +'\\'+file_name
    edit_file(file_path = file_path)