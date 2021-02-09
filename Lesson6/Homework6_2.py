'''
Урок 6. Задание №2
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
'''

class Road:
    _length = None
    _width = None
    __asphalt = 25 #кг
    __depth = 0.05 #м (в примере почему-то считаетмя 0,005, хотя 5 см это 0,05м)

    def __init__(self, length, width):
        self._width = width
        self._length = length

    def calculate(self):
        return self._length * self._width * self.__asphalt * self.__depth


road = Road(length=5000, width=20)
print(road.calculate())