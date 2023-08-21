import json
from googletrans import Translator

count = 0

def translate_json(json_file, lang="ar"):
    """Translates a JSON file to the specified language.

    Args:
        json_file: The path to the JSON file to translate.
        lang: The language to translate the file to.

    Returns:
        The translated JSON file as a string.
    """

    translator = Translator() # initialising the translator

    with open(json_file, "r") as f:
        json_data = json.load(f)

    translated_data = {}
    def trans(key, val):
        if type(val) == str:
            if val == "":
                print(key,':',val)
                return val
            else:
                if key in {"image", "id", "img", "langsuffix", "colorCode", "link", "logo"}:
                    print(key,':',val)
                    return val
                else:
                    translator.raise_Exception = True 
                    translated_value = translator.translate(val, src='en', dest=lang)
                    global count
                    count += 1
                    print(count)
                    print(key,':',translated_value.text)
                    return translated_value.text
        elif type(val) == dict:
            translated_dict = {}
            for key1, value1 in val.items():
                #print(key1, ':',value1)
                translated_dict[key1] = trans(key1, value1)
            translated_data[key] = translated_dict
        elif type(val) == list:
            pass
            # for itm in len(val):
            #     return trans(val[i])

    
    for key, value in json_data.items():
        translated_data[key] = trans(key, value)

    translated_file_name = f"{lang}.json"
    with open(translated_file_name, "w",encoding="utf-8") as f:
        json.dump(translated_data, f, ensure_ascii=False, indent=2)

    return translated_file_name

if __name__ == "__main__":
    json_file = "en2.json"
    lang = "ar"

    translated_file = translate_json(json_file, lang)

    print(f"Translated JSON saved as: {translated_file}")