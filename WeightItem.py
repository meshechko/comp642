#Student: Olexiy Meshechko, Student ID: 1148995

from Item import Item
import random

class WeightItem(Item):

    #constructor for UnitItem
    def __init__(self) -> None:
        Item.__init__(self)
        self.__weight = self.scale()

    #getter and setter for ProductWeight
    @property
    def ProductWeight(self) -> int:
        return self.__weight
    
    @ProductWeight.setter
    def ProductWeight(self, value: float) -> None:
        self.__weight = value

    #calculates cost of the weight item
    def calcCost(self) -> float:
        total = self._price * self.__weight
        return float(format(total, '.2f'))

    #represents the class object as a string
    def __str__(self) -> str:
        return f'{ self._name }: ${ self._price } x { self.__weight }kg = ${self.calcCost()}'

    #method to generate random number between 0.0 and 4.0
    def scale (self) -> float:
        value = random.uniform(0.0, 4.0)
        return float(format(value, '.2f'))

