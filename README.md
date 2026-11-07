# Виджет банковских операций клиента

## Установка
1. Клонируйте репозиторий.
2. Установите зависимости: 'poetry instaill'.

## Функционал
* Маскировка номеров карт и счетов ('src/widget.py').
* Формирование даты ('src/widget.py').
* Фильтрация операций по статусу ('src/processing.py').
* Сортировка операций по дате ('src/processing.py').

## Примеры использования

'''python
from src.processing import filter_by_state, sort_by_date

operations = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'DATE': '2018-09-12T21:27:25.241689'}
]

# Фильтрация
executed_ops = filter_by_state(operations) 
print(executed_ops)

# Сортировка
sorted_ops = sort_by_date(operations, reverse=False)
print(sorted_ops)
