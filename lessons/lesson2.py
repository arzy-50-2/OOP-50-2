from main import Hero
# import main
import random


# kirito = Hero("Kirito", 100)
# kirito.action()

# Наследование
# Полиморфизм


# Дочерний класс
class ShieldHero(Hero):

    def __init__(self,name, hp, lvl, mp):
        super().__init__(name, hp, lvl)
        self.mp = mp

    def action(self):
        return print(f"{self.name} берет шит")

hr = ShieldHero(name="name", mp=12, lvl=12, hp=12)
print(hr.attack())

# hr2 = Hero('Kirito')
# hr2.action()
