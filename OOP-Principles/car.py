"""Avtomobil ushın klass"""

class Car:
    __count = 0
    def __init__(self, company: str, model: str, color: str, km: int):
        self.kompaniya = company
        self.model = model
        self.ren = color
        self.__kilometer = km
        Car.__count += 1
        
    @classmethod
    def get_count(cls):
        return cls.__count

    def get_company(self):
        return self.kompaniya
    
    def get_model(self):
        return self.model
    
    def get_color(self):
        return self.ren
    
    def get_km(self):
        return self.__kilometer

    def set_company(self, new_company):
        self.kompaniya = new_company
        
    def set_model(self, new_model):
        self.model = new_model

    def set_color(self, new_color):
        self.ren = new_color
    
    def set_km(self, new_km):
        if new_km < 0:
            raise ValueError("Avtokóliktiń probegin qaytarıwǵa bolmaydı")
        self.__kilometer += new_km

cobalt = Car("Chevrolet", "Cobalt", "White", 200)
matiz = Car("Dewoo", "Matiz", "Green", 500)
damas = Car("Dewoo", "Damas", "white", 600)
print(Car.get_count())
print(cobalt.get_count())
print(damas.get_count())
