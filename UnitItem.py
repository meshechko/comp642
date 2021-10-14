from Item import Item

class UnitItem(Item):

    #constructor for UnitItem
    def __init__(self) -> None:
        self.__name = ''
        self.__price = 0
        self.__qty = 0
        

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
        print(type(price))
        if isinstance(price, float) and price > 0:
            self.__price = price
        else:
            raise ValueError('Incorrect value: price unit.')


    #getter and setter for myQuantity
    @property
    def Quantity(self) -> int:
        return self.__qty


    @Quantity.setter
    def Quantity(self, qty:int) -> None:
        if isinstance(qty, int) and qty > 0:
            self.__qty = qty
        else:
            raise ValueError('Incorrect value: quantity.')


    #calculates cost of the unit item
    def calcCost(self) -> float:
        return self.__price * self.__qty


    #represents the class object as a string
    def __str__(self) -> str:
        return f'{ self.__name }: ${ self.__price } x {self.__qty} = ${self.calcCost()}'
