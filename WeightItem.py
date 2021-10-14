# from _typeshed import SupportsReadline
from Item import Item
import random

class WeightItem(Item):

    #constructor for UnitItem
    def __init__(self) -> None:
        self.__prodName = ''
        self.__price = 0
        self.__weight = self.scale()


    @property
    def Name(self) -> str:
        return self.__name


    @Name.setter
    def Name(self, name:str) -> None:
        if name:
            self.__name = name
        else:
            raise ValueError('Incorrect value: product name.')


    @property
    def Price(self) -> str:
        return self.__prodName


    @Price.setter
    def Price(self, price:float) -> None:
        if isinstance(price, float) and price > 0:
            self.__price = price
        else:
            raise ValueError('Incorrect value: price.')


    #getter and setter for myWeight
    @property
    def ProductWeight(self) -> int:
        return self.__weight

    # @ProductWeight.setter
    # def ProductQuantity(self, qty:int) -> None:
    #     pass

    #calculates cost of the weight item
    def calcCost(self) -> float:
        return self.__price * self.__weight

    #represents the class object as a string
    def __str__(self) -> str:
        return f'{ self.__prodName }: ${ self.__price } x { self.__weight }kg = ${self.calcCost()}'

    #method to generate random number between 0.0 and 4.0
    def scale (self) -> float:
        value = random.uniform(0.0, 4.0)
        return float(format(value, '.2f'))

