from ShoppingCart import ShoppingCart
from typing import List
import math

class Customer:
    next_card_number = 10000
    #constructor
    def __init__(self, name:str) -> None:
        self.__cardNumber: int = Customer.next_card_number
        self.__clubPoint: int = 0
        self.__currentCart: ShoppingCart = None
        self.__cartList: List[ShoppingCart] = [] #previous shopping carts (excluding current)
        self.name = name
        Customer.next_card_number += 1
        self.__totalToDate: float = 0

    #getter and setter for customer's name
    @property
    def Name(self) -> str:
        return self.name

    @Name.setter
    def Name(self, name:str) -> None:
        self.name = name

    #getter for card number
    @property
    def CardNumber(self) -> str:
        return self.__cardNumber

    #getter and setter for club point
    @property
    def ClubPoint(self) -> str:
        return self.__clubPoint

    @ClubPoint.setter
    def ClubPoint(self, points:int) -> None:
        self.__clubPoint = points

    #getter for the current cart
    @property
    def CurrentCart(self) ->ShoppingCart:
        return self.__currentCart

    @CurrentCart.setter
    def CurrentCart(self, cart):
        self.__currentCart = cart

    #getter for the list of carts
    @property
    def CartList(self) -> List[ShoppingCart]:
        return self.__cartList

    #getter for the total purchase to date
    @property
    def TotalToDate(self) -> float:
        return self.__totalToDate

    @TotalToDate.setter
    def TotalToDate(self, value:float) -> None:
        self.__totalToDate = value

    #represents the class object as a string
    def __str__(self) -> str:
        return f'Customer: { self.Name }, card: { self.CardNumber }, club points: { self.ClubPoint }'

    #add current cart to the list of carts
    def addToCartList(self) -> None:
        self.__cartList.append(self.__currentCart)

    #update total purchase to date
    def updateTotal(self) -> None:
        self.TotalToDate += self.CurrentCart.calcTotalCost()

    #calculate club point for the current cart
    def calcClubPoint(self) -> int:
        clubPoints = self.CurrentCart.calcTotalCost() * 0.1 #1 point for each $10.00 spent at the supermarket
        return math.floor(clubPoints)

    #update the total club point
    def updateClubPoint(self) -> None:
        self.ClubPoint += self.calcClubPoint()

    #list the summary of all the previous transactions
    def custTrans(self) -> str:
        pass

    #List the details of all the previous transactions
    def custDetailTrans(self) -> str:
        pass

    #average cart total 
    def cartAverage(self) -> float:
        pass

