# ✅ **ШАГ 2: Научиться работать с методами**

# **Задача 2: "Калькулятор"**  
# Создай класс `Calculator` с методами:
# - `add(x, y)` — возвращает сумму
# - `subtract(x, y)` — возвращает разницу
# - `multiply(x, y)` — возвращает произведение
# - `divide(x, y)` — делит и обрабатывает ошибку деления на ноль

# **Зачем:** Чтобы научиться добавлять **логику** в методы и работать с ошибками.

# ---

class Calculator:
    def add(self, x, y):
        return x + y
    
    def substract(self, x, y):
        return x - y
    
    def multiply(self, x, y):
        return x * y
    
    def divide(self, x, y):
        if y == 0:
            raise ValueError("Нельзя делить на ноль")
        return x / y

calculator = Calculator()
result_add = calculator.add(5, 3)
result_sub = calculator.substract(10, 4)
result_mult = calculator.multiply(2, 6)
result_divide = calculator.divide(10, 2)
print(result_add, result_sub, result_mult, result_divide)