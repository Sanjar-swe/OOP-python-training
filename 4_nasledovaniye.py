# ✅ **ШАГ 4: Наследование**

# **Задача 4: "Транспорт"**  
# Создай класс `Vehicle` с атрибутами `brand`, `model`.  
# Создай класс `Car`, который наследует `Vehicle`, добавляя атрибут `number_of_doors`.

# Добавь метод `display_info()` в `Car`, который печатает полную информацию.

# **Зачем:** Чтобы увидеть, как **наследовать** и **расширять** функциональность без копирования кода.

# ---

class Vehicle:
    brand: str
    model: str
    
class Car(Vehicle): # <- Наследуемся от Vehicle
    number_of_doors: int
    
    def display_info(self):
        print(f"{self.brand} {self.model}, {self.number_of_doors} doors")
        
car = Car()
car.brand = "Toyota"
car.model = "Camry"
car.number_of_doors = 4
car.display_info()