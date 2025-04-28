#republic, region, city, street, home number

class Address:
    def __init__(self, republic, region, city, street, home_number):
        self.republic = republic
        self.region = region
        self.city = city
        self.street = street
        self.home_number = home_number  
    
    
    #setters
    def set_republic(self, republic):
        self.republic = republic
        
    def set_region(self, region):
        self.region = region
        
    def set_city(self, city):
        self.city = city
        
    def set_street(self, street):
        self.street = street
        
    def set_home_number(self, home_number):
        self.home_number = home_number
    
    #getters
    def get_republic(self):
        return self.republic
    
    def get_region(self):
        return self.region
    
    def get_city(self):
        return self.city
    
    def get_street(self):
        return self.street
    
    def get_home_number(self):
        return self.home_number
    
    #get full address
    def get_full_address(self):
        return(f"{self.republic}, {self.region}, {self.city}, {self.street}, {self.home_number}")
    
adress = Address("Belarus", "Minsk", "Minsk", "Lenina", 1)

print(adress.get_full_address())
