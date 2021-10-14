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
            raise ValueError('Incorrect value: product.')
    

    @property
    def Price(self) -> str:
        return self.__prodName


    @Price.setter
    def Price(self, price:float) -> None:
        # I have added "if-else" validation into "UnitItem class" to check if price value is float
        # TK Inter always returs a string from input field, so if users enter text in price field then without "try" block it shows an error.
        # How can I avoid this try/except block in "UnitItem" class?
        error = 'Incorrect value: price per unit.'
        try:
            price = float(price)
            if price > 0:
                self.__price = float(price)
            else:
                raise ValueError(error)
        except:
            raise ValueError(error)


    #getter and setter for myQuantity
    @property
    def Quantity(self) -> int:
        return self.__qty


    @Quantity.setter
    def Quantity(self, qty:int) -> None:
        error = 'Incorrect value: number of units.'
        try:
            qty = int(qty)
            if qty > 0:
                self.__qty = int(qty)
            else:
                raise ValueError(error)
        except:
            raise ValueError(error)

    #calculates cost of the unit item
    def calcCost(self) -> float:
        return self.__price * self.__qty


    #represents the class object as a string
    def __str__(self) -> str:
        return f'{ self.__name }: ${ self.__price } x {self.__qty} = ${self.calcCost()}'
