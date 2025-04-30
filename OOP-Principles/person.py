from datetime import date


class Person:
    def __init__(
        self, 
        first_name: str, 
        last_name: str, 
        birth_date: date,
        ID: int
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.__ID = ID
        
    def set_first_name(self, first_name: str) -> None:
        self.first_name = first_name
        
    def set_last_name(self, last_name: str) -> None:
        self.last_name = last_name
        
    def set_birth_date(self, birth_date: date) -> None:
        self.birth_date = birth_date
    
    def set_id(self, ID: int) -> None:
        self.__ID = ID
    
    def get_first_name(self) -> str:
        return self.first_name
    
    def get_last_name(self) -> str:
        return self.last_name
    
    def get_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    def get_birth_date(self) -> date:
        return self.birth_date
    
    def get_id(self) -> int:
        return self.__ID
