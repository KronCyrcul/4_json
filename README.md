# Форматирование JSON

Программа на входе принимает путь до файла JSON и выводит в консоль его содержимое в более удобном для читателя виде.   
Пример исходного файла:
```javascript
[{"Id":"79742784-9ef3-4543-bc98-a219a8903c18","Number":1,"Cells":{"global_id":14371450,"Name":"Ароматный Мир","IsNetObject":"да","OperatingCompany":"Ароматный Мир","TypeService":"реализация продовольственных товаров","Address":"улица Академика Павлова, дом 10"}}]
```

Пример измененного файла
```javascript
[
    {
        "Cells": {
            "Address": "улица Академика Павлова, дом 10",
            "IsNetObject": "да",
            "Name": "Ароматный Мир",
            "OperatingCompany": "Ароматный Мир",
            "TypeService": "реализация продовольственных товаров",
            "global_id": 14371450
        },
        "Id": "79742784-9ef3-4543-bc98-a219a8903c18",
        "Number": 1
    }
]
```

# Quickstart

Example of script launch on Linux, Python 3.5:

```bash

$ python pprint_json.py <path to file>
#пример вывода текста
[
    {
        "Cells": {
            "Address": "улица Академика Павлова, дом 10",
            "IsNetObject": "да",
            "Name": "Ароматный Мир",
            "OperatingCompany": "Ароматный Мир",
            "TypeService": "реализация продовольственных товаров",
            "global_id": 14371450
        },
        "Id": "79742784-9ef3-4543-bc98-a219a8903c18",
        "Number": 1
    }
]
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
