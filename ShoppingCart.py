from typing import List
from UnitItem import UnitItem
from WeightItem import WeightItem
from Item import Item
from datetime import date, datetime

class ShoppingCart:

    #constructor
    def __init__(self) -> None:
        self.__purchaseDate : str = datetime.now().strftime("%d/%m/%Y")
        self.__items = []

    #getter for purchase date
    @property
    def PurchaseDate(self) -> datetime:
        return self.__purchaseDate

    #getter for list of items in the cart
    @property
    def Items(self) -> List[Item]:
        return self.__items

    #represents the class object as a string
    def __str__(self) -> str:
        return f'Items: { ",".join(self.__items) }, date: { self.__purchaseDate }, { self.calcTotalCost() }'

    #adds unit item to the cart and returns the cost
    def addUnitItem(self, unitItem:UnitItem) -> float:
        self.__items.append(unitItem)
        return unitItem.calcCost()

    #adds weight item to the cart and returns the cost
    def addWeightItem(self, weightItem:WeightItem) -> float:
        self.__items.append(weightItem)
        return weightItem.calcCost()

    #calculate the total cost of the items in the cart
    def calcTotalCost(self) -> float:
        total = 0
        for item in self.__items:
            total += item.calcCost()
        return total