import json
from googletrans import Translator

def translate_json(json_file, lang="ar"):
    """Translates a JSON file to the specified language.
    
    Args:
        json_file: The path to the JSON file to translate.
        lang: The language to translate the file to.
    
    Returns:
        The translated JSON file as a string.
    """
    
    translator = Translator()
    
    with open(json_file, "r", encoding="utf-8") as f:
        json_data = json.load(f)

    def trans(value):
        if isinstance(value, str):
            if value == "":
                return value
            else:
                translated_value = translator.translate(value, src='en', dest=lang)
                return translated_value.text
        elif isinstance(value, dict):
            translated_dict = {}
            for key1, value1 in value.items():
                translated_dict[key1] = trans(value1)
                print(key1, value1)
            return translated_dict
        elif isinstance(value, list):
            pass
            # translated_list = []
            # for item in value:
            #     translated_list.append(trans(item))
            # return translated_list
        else:
            return value
    
    translated_data = trans(json_data)
    
    translated_file_name = f"{lang}.json"
    with open(translated_file_name, "w", encoding="utf-8") as f:
        json.dump(translated_data, f, ensure_ascii=False, indent=2)
    
    return translated_file_name

if __name__ == "__main__":
    json_file = "en.json"
    lang = "ar"
    
    translated_file = translate_json(json_file, lang)
    
    print(f"Translated JSON saved as: {translated_file}")
