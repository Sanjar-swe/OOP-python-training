"""Avtomobil ushin klass"""
# """magic methods"""
class Car:
    def __init__(self, company: str, model: str, color: str, km: int):
        self.kompaniya = company
        self.model = model
        self.ren = color
        self.kilometr = km
    def get_company(self):
        return self.kompaniya
    
    def get_model(self):
        return self.model
    
    def get_km(self):
        return self.kilometr
        
        
    def get_color(self):
        return self.ren
    
    def set_km(self, new_km):
        if new_km < 0:
            raise ValueError("Mashinnin' probegin qaytariwg'a bolmaydi")
        self.kilometr += new_km
    
    def set_company(self, new_company):
        self.kompaniya = new_company
        
    def set_company(self, new_company):
        self.kompaniya = new_company
    def set_color(self, new_color):
        self.ren = new_color
        
    
    
cobalt = Car("Chevrolet", "Cobalt", "White", 200)
# print(cobalt.get_company())
cobalt.set_km(10)
print(cobalt.get_km())

#getter setter
