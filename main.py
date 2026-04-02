#  класс Hero
class Hero:
    # Конструктор
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    # Метод приветствия
    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    # Метод атаки
    def attack(self):
        print(f"{self.name} наносит удар!")
        self.strength -= 1  # Уменьшаем силу на 1

    # Метод отдыха
    def rest(self):
        print(f"{self.name} отдыхает…")
        self.health += 1    # Увеличиваем здоровье на 1


# Создание 2 объекта класса Hero
hero1 = Hero("Арагорн", 10, 100, 50)
hero2 = Hero("Леголас", 12, 80, 45)

# Проверка первого героя
print(f"--- Тест для {hero1.name} ---")
hero1.greet()
print(f"Сила до атаки: {hero1.strength}")
hero1.attack()
print(f"Сила после атаки: {hero1.strength}")

print(f"Здоровье до отдыха: {hero1.health}")
hero1.rest()
print(f"Здоровье после отдыха: {hero1.health}")

print("\n")

# Проверка второго героя
print(f"--- Тест для {hero2.name} ---")
hero2.greet()
print(f"Сила до атаки: {hero2.strength}")
hero2.attack()
print(f"Сила после атаки: {hero2.strength}")

print(f"Здоровье до отдыха: {hero2.health}")
hero2.rest()
print(f"Здоровье после отдыха: {hero2.health}")