#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def find_product_between_max_min(*args):
    """
    Находит произведение аргументов, расположенных между максимальным и минимальным аргументами.
    """
    if not args:
        return None  # В случае отсутствия аргументов возвращаем None

    # Находим индексы максимального и минимального аргументов
    max_index = args.index(max(args))
    min_index = args.index(min(args))

    # Определяем начальный и конечный индексы для расчета произведения
    start_index = min(max_index, min_index) + 1
    end_index = max(max_index, min_index)

    # Исключаем случай, когда начальный и конечный индексы совпадают
    if start_index == end_index:
        return None

    # Вычисляем произведение аргументов
    product = 1
    for i in range(start_index, end_index):
        product *= args[i]

    return product

if __name__ == "__main__":
    result = find_product_between_max_min(3, 5, 2, 8, 4, 10)
    print("Произведение аргументов между максимальным и минимальным:", result)
