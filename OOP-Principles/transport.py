
class Transport:
    def __init__(self, number: int):
        self.number = number
    
    def move(self):
        return "moving"


class Train(Transport):
    def __init__(self, number):
        super().__init__(number)
        
    def move(self):
        return "tutudut"

class Airplane(Transport):
    def __init__(self, number):
        super().__init__(number)
    
    def move(self):
        return "flying"

train = Train(12)
airplane = Airplane(443)
print(train.move())
print(airplane.move())