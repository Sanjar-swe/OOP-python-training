# republic, region, city, street, home number

class Address:
    
    def __init__(self, republic: str, region: str, city: str, street: str, home_number: int) -> None:
        self.republic = republic
        self.region = region
        self.city = city
        self.street = street
        self.home_number = home_number
    
    def set_republic(self, republic: str) -> None:
        self.republic = republic
        
    def set_region(self, region: str) -> None:
        self.region = region
        
    def set_city(self, city: str) -> None:
        self.city = city
        
    def set_street(self, street: str) -> None:
        self.street = street
    
    def set_home_number(self, home_number: int) -> None:
        self.home_number = home_number
    
    def get_republic(self) -> str:
        return self.republic
    
    def get_region(self) -> str:
        return self.region
    
    def get_city(self) -> str:
        return self.city
    
    def get_street(self) -> str:
        return self.street
    
    def get_home_number(self) -> int:
        return self.home_number
    
    def get_full_address(self):
        # info = f"{self.get_republic()}, "
        # info += f"{self.get_region()}, "
        # info += f"{self.get_city()}, "
        # info += f"{self.get_street()}, "
        # info += f"{self.get_home_number()}"
        # return info
        
        return f"{self.get_republic()}, " \
            f"{self.get_region()}, " \
            f"{self.get_city()}, " \
            f"{self.get_street()}, " \
            f"{self.get_home_number()}"

adderss = Address("Uzbekistan", "Republic of Karakalpakstan", "Nukus", "A.Dosnazarov", 23)
print(adderss.get_full_address())