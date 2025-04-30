"""OBYEKTKE BAǴDARLANǴAN PROGRAMMALASTÍRÍW"""
"""OBJECT ORIENTED PROGRAMMING (OOP)"""

# CLASS & OBJECT
# CLASS: ATRIBUTE & METHOD

# from person import Person

# adam = Person("Abiw", 1999, "Nókis")
# adam_2 = Person("Amanjol", 1986, "Shomanay")

# print(adam_2.say_name())
# print(adam.calculate_age())
# print(adam.get_info())


"""TIYKARǴÍ PRINCPLER"""
# Miyrasxorlıq, Polimorfizm, Inkapsuliyaciya, Abstrakciya

from person import Person
from datetime import date


person = Person("John", "Doe", date(2000, 10, 20), 131223243)
print(person.get_full_name())
