# #OOP
#
# #класс
# class Person:
#
#
#     def __init__(self, name, age=0 ,city="none"):
#         #атрибуты класса
#         self.name = name
#         self.age = age
#         self.city = city
#
#
#     def introduce(self):
#         print(f"привет, меня зовут {self.name}, мне {self.age},я живу в городе {self.city}")
#
#
# #объекты класса(экземпляры класса
# person_one = Person("Ардагер",25,"bishkek")
# person_second = Person(name="John Doe",age=33,city="none")
#
# print(person_one.age)
# person_one.introduce()
# print(person_second)


#homework_1

class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def introduce(self):
        print(f"привет, меня зовут {self.name}, мой lvl {self.lvl}, мое hp {self.hp}")

    def is_adult(self):
        return self.lvl >= 10

    def __str__(self):
        return f"Имя: {self.name}, lvl: {self.lvl}, HP: {self.hp}"


hero1 = Hero("Артур", 5, 100)
hero2 = Hero("Ланселот", 15, 150)
hero3 = Hero("Джон",7, 100)
hero1.introduce()
print(hero1.is_adult())  # False
print(hero2.is_adult())  # True
print(hero3)