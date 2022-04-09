class Car:
    def __init__(self, color=None, type_car=None, year=None):
        self.color = color
        self.type_car = type_car
        self.year = year

    def engineOn(self):
        return f'Автомобиль {self.color} {self.type_car} {self.year} года заведен!'

    def engineOff(self):
        return f'Автомобиль {self.color} {self.type_car} {self.year} года заглушен!'

    def setTypeCar(self, type_car):
            self.type_car = type_car
            return 'Тип присвоен'

    def setColor(self, color):
            self.color = color
            return 'Цвет присвоен'

    def setYear(self, year):
            self.year = year
            return 'Год присвоен'

car_1 = Car(color='красный',type_car='седан')
print(car_1 .engineOn())
print(f' {car_1.setTypeCar("джип")}, {car_1.setColor("черный")},{car_1.setYear(1999)}')
print(car_1.engineOff(),'\n')

car_2 = Car('белый','универсал',2001 )
print(car_2.engineOn())
print(f'{car_2.setTypeCar("седан")}.')
print(car_2.engineOff())