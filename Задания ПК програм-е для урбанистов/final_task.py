import csv
from typing import List, Dict

def read_file(housing_data: str) -> List[Dict]:
    """Читает данные из CSV файла и преобразует их в список словарей.

    :param filename: Название файла, содержащего данные.
    :return: Список словарей с данными о домах.
    """
    houses = []
    with open(housing_data, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            house = {
                "area_id": row["area_id"],
                "house_address": row["house_address"],
                "floor_count": int(row["floor_count"]),
                "heating_house_type": row["heating_house_type"],
                "heating_value": float(row["heating_value"]),
                "area_residential": float(row["area_residential"]),
                "population": int(row["population"])
            }
            houses.append(house)
    return houses

def classify_house(floor_count: int) -> str:
    """Классифицирует дом на основе количества этажей.

    Проверяет, является ли количество этажей целым числом и положительным значением.
    Возвращает категорию дома в зависимости от количества этажей.

    :param floor_count: Количество этажей в доме.
    :return: Категория дома в виде строки: "Малоэтажный", "Среднеэтажный" или "Многоэтажный".
    """
    if not isinstance(floor_count, int):
        raise TypeError("Количество этажей должно быть целым числом.")
    if floor_count <= 0:
        raise ValueError("Количество этажей должно быть положительным числом.")

    if floor_count <= 5:
        return "Малоэтажный"
    elif 6 <= floor_count <= 16:
        return "Среднеэтажный"
    else:
        return "Многоэтажный"

def get_classify_houses(houses: List[Dict]) -> List[str]:
    """Классифицирует дома на основе количества этажей.

    :param houses: Список словарей с данными о домах.
    :return: Список категорий домов.
    """
    categories = [classify_house(house["floor_count"]) for house in houses]
    return categories

def get_count_house_categories(categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество домов в каждой категории.

    :param categories: Список категорий домов.
    :return: Словарь с количеством домов в каждой категории.
    """
    count = {}
    for category in categories:
        if category in count:
            count[category] += 1
        else:
            count[category] = 1
    return count

def min_area_residential(houses: List[Dict]) -> str:
    """Находит адрес дома с наименьшим средним количеством квадратных метров жилой площади на одного жильца.

    :param houses: Список словарей с данными о домах.
    :return: Адрес дома с наименьшим средним количеством квадратных метров жилой площади на одного жильца.
    """
    min_avg_area_per_person = float('inf')
    min_avg_area_house_address = ""

    for house in houses:
        avg_area_per_person = house["area_residential"] / house["population"]
        if avg_area_per_person < min_avg_area_per_person:
            min_avg_area_per_person = avg_area_per_person
            min_avg_area_house_address = house["house_address"]

    return min_avg_area_house_address

if __name__ == "__main__":
    # Файл с данными
    filename = "housing_data.csv"

    # Чтение данных из файла
    houses = read_file(filename)

    # Классификация домов
    house_categories = get_classify_houses(houses)

    # Подсчёт количества домов в каждой категории
    house_count_by_category = get_count_house_categories(house_categories)

    # Поиск дома с наименьшим средним количеством кв.м на одного жителя
    house_with_min_avg_area = min_area_residential(houses)

    # Вывод информации
    print("Количество домов по категориям:")
    for category, count in house_count_by_category.items():
        print(f"{category}: {count}")

    print(f"\nДом с наименьшим средним количеством кв.м на одного жителя: {house_with_min_avg_area}")
