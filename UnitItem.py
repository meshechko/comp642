#Student: Olexiy Meshechko, Student ID: 1148995

from Item import Item

class UnitItem(Item):

    #constructor for UnitItem
    def __init__(self) -> None:
        Item.__init__(self)
        self.__qty = 0

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
        total = self._price * self.__qty
        return float(format(total, '.2f'))


    #represents the class object as a string
    def __str__(self) -> str:
        return f'{ self._name }: ${ self._price } x {self.__qty} = ${self.calcCost()}'
