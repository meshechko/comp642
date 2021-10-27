#Student: Olexiy Meshechko, Student ID: 1148995

from abc import ABC, abstractmethod

class Item (ABC):

    #constructor 
    def __init__(self) -> None:
        self._name = ''
        self._price = 0
    
    @property
    def Name(self) -> str:
        return self._name


    @Name.setter
    def Name(self, name:str) -> None:
        if name:
            self._name = name
        else:
            raise ValueError('Incorrect value: product name.')
    

    @property
    def Price(self) -> str:
        return self._price


    @Price.setter
    def Price(self, price:float) -> None:
        error = 'Incorrect value: price per unit.'
        try:
            price = float(price)
            if price > 0:
                self._price = price
            else:
                raise ValueError(error)
        except:
            raise ValueError(error)

    #abstract method to calculate cost of the item
    @abstractmethod
    def calcCost(self) -> float:
        pass

    #represents the class object as a string
    def __str__(self) -> str:
        pass



    