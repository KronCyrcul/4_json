import json
import sys


def load_data(filepath):
    try:
        with open(filepath, encoding="utf-8") as file:
            json_content = json.loads(file.read())
        return json_content
    except json.decoder.JSONDecodeError:
        return None


def pretty_print_json(json_string):
    return json.dumps(json_string, separators=(",", ":"), indent=4,
        sort_keys=True, ensure_ascii=False)


if __name__ == '__main__':
    try:
        filepath = sys.argv[1]
        json_content = load_data(filepath)
        if json_content is None:
            sys.exit("Неверный файл")
        print(pretty_print_json(json_content))
    except (IndexError, FileNotFoundError):
        sys.exit("Введите путь до файла json")
