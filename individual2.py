#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
#   В списке, состоящем из целых элементов, вычислить номер максимального элемента списка;
if __name__ == '__main__':
    a = list(map(int, input("Введите список: ").split()))
    if not a:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)

    a_max = a[0]
    position = 0

    #   Номер максимального элемента списка
    for i, item in enumerate(a):
        if item > a_max:
            position, a_max = i, item
    print("Номер максимального элемента списка: ", position)