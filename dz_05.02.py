class Flower:
  type = 0
  freshness = 0
  stalks = 0
  __number = 0

def __init__(self, number0):
    self.__number = number0

    # чтение инкапсулированной массы
def get_number(self):
    return self.__number

class Chrisantema (Flower):
    season = 0

class Rose (Flower):
    __packs = 0
    def __init__(self, number0):
        Flower.__init__(self, number0)
        self.__packs = number0//5

    # чтение инкапсулированного числа мест
    def get_packs(self):
        return self.__packs

class Bouquet:
    __MaxNumber = 0
    __flowers = []
