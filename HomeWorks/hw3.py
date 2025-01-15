from main import Hero

class Jester(Hero):
    def __init__(self,name):
        super().__init__(name)
    def unique_attack(self):
        print(f"{self.name} использует уникальную атаку — Псевдонажмутие!")


    def unique_scream(self):
        print(f"{self.name} кричит: \"Смех победит!\"")


    def action(self):
        random_choice = self.get_random_int()
        print(f"Случайный выбор: {random_choice}")

        if random_choice == 1:
            self.attack()
        elif random_choice == 2:
            self.protection()
        else:
            self.rest()

if __name__ == "__main__":
    jester = Jester("Джестер")
    jester.unique_attack()
    jester.unique_scream()
    jester.action()