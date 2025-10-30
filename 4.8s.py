import csv
from functools import reduce
import os


def read_csv(filename):

    with open(filename, 'r', encoding='utf-8') as file:
        return list(csv.DictReader(file))


def create_sample_csv(filename):

    sample_data = [
        {'name': 'Alice', 'age': '25', 'salary': '50000', 'department': 'IT'},
        {'name': 'Bob', 'age': '30', 'salary': '45000', 'department': 'HR'},
        {'name': 'Charlie', 'age': '35', 'salary': '70000', 'department': 'IT'},
        {'name': 'Diana', 'age': '28', 'salary': '55000', 'department': 'Finance'},
        {'name': 'Eve', 'age': '22', 'salary': '40000', 'department': 'IT'},
    ]

    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=sample_data[0].keys())
        writer.writeheader()
        writer.writerows(sample_data)

    print(f"Создан новый файл {filename} с тестовыми данными")
    return sample_data


def load_or_create_data(filename):

    if os.path.exists(filename):
        print(f"Файл {filename} уже существует, читаем данные из него")
        return read_csv(filename)
    else:
        print(f"Файл {filename} не найден, создаем новый")
        create_sample_csv(filename)
        return read_csv(filename)


def process_csv_data(data, filters=None, transformations=None):

    if filters:
        data = reduce(lambda acc, f: list(filter(f, acc)), filters, data)

    if transformations:
        data = list(map(
            lambda row: reduce(lambda r, t: t(r), transformations, row),
            data
        ))

    return data

if __name__ == "__main__":
    filename = 'employees.csv'

    data = load_or_create_data(filename)

    print(f"\nЗагружено {len(data)} сотрудников:")
    for row in data:
        print(f"  - {row['name']}, {row['age']} лет, {row['salary']} руб, {row['department']}")

    filters = [
        lambda row: int(row['age']) > 25,
        lambda row: row['department'] == 'IT',
    ]

    transformations = [
        lambda row: {**row, 'salary': int(row['salary']) * 1.1},
        lambda row: {**row, 'age_group': 'Senior' if int(row['age']) > 30 else 'Junior'},
        lambda row: {k: v for k, v in row.items() if k != 'department'},
    ]

    processed_data = process_csv_data(data, filters, transformations)

    print(f"\nОбработанные данные (осталось {len(processed_data)} сотрудников):")
    for row in processed_data:
        print(row)