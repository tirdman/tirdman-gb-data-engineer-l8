"""
Задание 2.

Реализовать проект расчета суммарного расхода ткани на производство одежды.

Единственный класс этого проекта — одежда (класс Clothes).

К типам одежды в этом проекте относятся пальто и костюм.

У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: v и h, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (v/6.5 + 0.5),
для костюма (2*h + 0.3). Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать
абстрактный класс для единственного класса проекта,
проверить на практике работу декоратора @property

Пример:
Расход ткани на пальто = 1.27
Расход ткани на костюм = 20.30
Общий расход ткани = 21.57
"""

from functools import reduce

from abc import ABC, abstractmethod


class ClothesInterface(ABC):

    @abstractmethod
    def get_clothes_rate(self):
        pass


class Clothes(ClothesInterface):
    close_items = []

    def __init__(self, clothes_type, clothes_size):
        self.close_type = clothes_type
        self.clothe_size = clothes_size

        Clothes.close_items.append(self)

    @property
    def get_clothes_rate(self):
        if self.close_type == 'coat':
            return self.clothe_size / 6.5 + 0.5

        return 2 * self.clothe_size + 0.3

    @staticmethod
    def get_clothes_rate_all():
        all_rate = 0
        for next_item in Clothes.close_items:
            all_rate += next_item.get_clothes_rate
        return all_rate


coat = Clothes('coat', 52)
suite = Clothes('suite', 180)

for next_item_clothes in Clothes.close_items:
    print(f"Расход на {next_item_clothes.close_type}: {next_item_clothes.get_clothes_rate}")

print()

print(f"Общий расход: {Clothes.get_clothes_rate_all()}")
