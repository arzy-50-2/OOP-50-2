class Heroes:
    def __init__(self, name, hp):
        self.name = name  # Имя героя
        self.hp = hp      # Количество здоровья

    def action(self):
        print(f"{self.name} делает какое-то действие.")

    def attack(self):
        print(f"{self.name} атакует!")

class Archer(Heroes):
    def __init__(self, name, hp, arrows, precision):
        super().__init__(name, hp)
        self.arrows = arrows
        self.precision = precision

    def attack(self):
        if self.arrows > 0:
            self.arrows -= 1
            if self.precision >= 75:
                print(f"{self.name} выстрелил и попал в цель!")
            else:
                print(f"{self.name} выстрелил, но промахнулся!")
        else:
            print(f"{self.name} не может атаковать, так как у него нет стрел!")

    def rest(self):
        self.arrows += 5
        print(f"{self.name} отдыхает и пополняет стрелы. Теперь у него {self.arrows} стрел.")

    def status(self):
        return (f"Имя: {self.name}, Здоровье: {self.hp}, Стрелы: {self.arrows}, Точность: {self.precision}%")

archer = Archer(name="Лукас", hp=100, arrows=10, precision=80)

archer.action()
archer.attack()
archer.rest()
print(archer.status())
archer.attack()