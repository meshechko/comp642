from abc import ABC, abstractmethod

class Item (ABC):

    #constructor 
    def __init__(self, prodName:str, price:float) -> None:
        self._myProdName = prodName
        self._myPrice = price
    
    #getter and setter for myProdName
    @property
    def ProductName(self) -> str:
        pass
    
    @ProductName.setter
    def ProductName(self, value:str) -> None:
        pass

    #getter and setter for myPrice
    @property
    def ProductPrice(self) -> float:
        pass

    @ProductPrice.setter
    def ProductPrice(self, value:float) -> None:
        pass

    #abstract method to calculate cost of the item
    @abstractmethod
    def calcCost(self) -> float:
        pass

    #represents the class object as a string
    def __str__(self) -> str:
        pass



    