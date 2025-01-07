# OOP
#
# First Class
# FLAT - Плоская
# SRC - Исходный
# add_number
# AddNumber -
import random

# Родительский класс
class Hero:

    def __init__(self, name, hp=100, lvl=1):
        # атрибуты класса
        self.name = name
        self.hp = hp
        self.lvl = lvl

    def action(self):
        return print(f"{self.name} делает первый шаг")

    def attack(self):
        return print(f"{self.name} базавая атака")

    def rest(self):
        self.hp += random.randint(0, 100)

        return print(f"{self.name} rest and reset hp {self.hp}")
