import json
import sys


def load_data(filepath):
    try:
        with open(filepath, encoding="utf-8") as file:
            bars_data = json.loads(file.read())
        return bars_data
    except json.decoder.JSONDecodeError:
        return None

        
def pretty_print_json(data):
    return json.dumps(data,separators=(",",":"),indent=4,sort_keys=True,ensure_ascii=False)


if __name__ == '__main__':
    try:
        filepath = sys.argv[1]
        json_string = load_data(filepath)
        if json_string == None:
            sys.exit("Неверный файл")
        print(pretty_print_json(json_string))
    except (IndexError, FileNotFoundError):
        sys.exit("Введите путь до файла json")
    