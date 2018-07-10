import json
import sys


def load_data(filepath):
    try:
        with open(filepath, encoding="utf-8") as file:
            file_content = json.loads(file.read())
        return file_content
    except json.decoder.JSONDecodeError:
        return None

 
def pretty_print_json(file_content):
    return json.dumps(file_content, separators=(",", ":"), indent=4,
        sort_keys=True, ensure_ascii=False)


if __name__ == "__main__":
    try:
        filepath = sys.argv[1]
        file_content = load_data(filepath)
        if file_content is None:
            sys.exit("Неверный файл")
        print(pretty_print_json(file_content))
    except (IndexError, FileNotFoundError):
        sys.exit("Введите путь до файла json")
