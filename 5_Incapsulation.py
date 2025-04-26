# ✅ **ШАГ 5: Инкапсуляция (скрытие данных)**

# **Задача 5: "Банк"**  
# Создай класс `BankAccount`:
# - приватный атрибут `_balance`
# - методы `deposit(amount)` и `withdraw(amount)`
# - метод `get_balance()`, который возвращает баланс

# **Зачем:** Чтобы понять, как **скрывать важные данные** от внешнего вмешательства.

# ---

class BankAccount:
    def __init__(self, balance: float):
        self._balance = balance # <- приватный атрибут

    def get_balance(self):
        return self._balance
    
    def deposit(self, amount: float):
        self._balance += amount
    
    def withdraw(self, amount: float):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Недостаточно средств")
#(__balance)
# Python начнёт маскировать это имя внутри класса (механизм называется Name Mangling) 
account = BankAccount(1000)
print(account.get_balance()) # 1000
account.deposit(500)
print(account.get_balance()) #1500


# ✨ Кратко:

# Название	Что значит
# balance	Обычный атрибут (публичный)
# _balance	Полу-приватный (не трогай напрямую - договор между программистами)
# __balance	Реально спрятанный (name mangling)
