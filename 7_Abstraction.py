from abc import ABC, abstractmethod

# # 🎯 Мини-проект на Абстракцию: **"Транспортная система"**

# ## 📋 Условие:
# Тебе нужно **спроектировать** (на бумаге или в голове, без кода) структуру для системы управления разным транспортом.

# ---
# ## 📦 Что должно быть:

# ### 1. Абстрактный класс `Transport`:
# - Описание: это общий план для любого транспорта.
# - Методы (без реализации):
#   - `start()` — начать движение
#   - `stop()` — остановить движение
#   - `fuel_up()` — заправиться
class Transport(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    
    def stop(self):
        pass
    @abstractmethod
    
    def fuel_up(self):
        pass
# ---

# ### 2. Классы-наследники:
# - `Car` (машина)
# - `Bike` (велосипед)
# - `Boat` (лодка)
class Car(Transport):
    def start(self):
        print("Car starts moving by pressing the accelerator pedal")
    
    def stop(self):
        print("Car stops moving by pressing the brake pedal")
        
    def fuel_up(self):
        print("Car is fueled by gasoline")
#
class Bike(Transport):
    def start(self):
        print("Bike starts moving by pedaling")
        
    def stop(self):
        print("Bike stops moving by braking")
    def fuel_up(self):
        print("Bicycles don't need fuel.")
#
class Boat(Transport):
    def start(self):
        print("Boat starts moving by pushing the oars")
    
    def stop(self):
        print("Boat stops moving by pulling the oars")
        
    def fuel_up(self):
        print("Boats are fueled by diesel")
# Каждый из них **реализует** свои версии методов:
# - Например, **велосипед** заправляться не должен!  
#   Значит метод `fuel_up()` можно сделать так, чтобы он писал: `"Bicycles don't need fuel."`
    
# ---

# ## 🎯 Конечная цель:

# 1. Ты **описываешь**, какие методы в каком классе будут работать по-своему.
# 2. Ты **понимаешь**, что все классы работают по **одинаковому интерфейсу** (`start`, `stop`, `fuel_up`), хотя они совершенно разные внутри.

# ---

# # 📋 Чек-лист выполнения задания:

# - [ ] Назови абстрактный класс `Transport`
# - [ ] Назови хотя бы 3 транспорта-наследника
# - [ ] Придумай, что делает каждый метод `start()`, `stop()`, `fuel_up()` для разных транспортов
# - [ ] Пойми: зачем удобно обращаться к любому транспорту через общие методы

# ---

# # 📚 [Как должен мыслить эксперт при выполнении такого задания:]

# - "Я хочу сделать систему, где **всё выглядит одинаково** снаружи (`start`, `stop`, `fuel_up`), но **ведёт себя по-разному** внутри."
# - "Мне надо сначала продумать, какие действия общие для всех транспортов."
# - "Я должен скрыть детали реализации и оставить только общие действия."

# ---

# 💬 Если хочешь, после выполнения я могу ещё предложить тебе **уровень 2** сложности:  
# **"Добавить разные типы топлива и методы проверки состояния транспорта."** 🚀  

# Сказать сразу условия уровня 2? 🔥  
# (Он прям прокачает тебя на практическое понимание Абстракций!)