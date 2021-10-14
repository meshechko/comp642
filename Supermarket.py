from Customer import Customer
from ShoppingCart import ShoppingCart
from UnitItem import UnitItem
from WeightItem import WeightItem
from typing import List

class Supermarket:

    #constructor
    def __init__(self) -> None:
        self.__customers: List[Customer] = []

    #getter for the list of customers
    @property 
    def CustomerList(self) -> List[Customer]:
        return self.__customers

    def getCustomerNames(self):
        names = []
        for customer in self.__customers:
            names.append(customer.Name)
        return names

     # read customers from txt
    def loadCustomers(self):
        with open('Customers.txt', 'r') as f: 
            lines = f.readlines()
            for line in lines:
                data = line.split(',')
                name = data[0]
                self.addCustomer(name)

    #creates and adds new customer to the customer list
    def addCustomer(self, name:str):
        self.__customers.append(Customer(name))

    # finds a customer object based on a customer's name
    def findCustomer(self, cname:str) -> Customer:
        for customer in self.__customers:
            if cname.lower() in customer.Name.lower():
                return customer

    # finds a customer's card number based on a customer's name
    def getCustomerID(self, cname:str) -> int:
        for customer in self.__customers:
            if cname.lower() in customer.Name.lower():
                return customer.CardNumber

    # gets the club point for a selected customer 
    def getCustomerClubPoint(self, cname:str) -> int:
        customer = self.findCustomer(cname)
        return customer.ClubPoint

    # adds unit item to the customer's current cart and returns the cost
    def addCustUnitItem(self, cname:str, prod:str, price:float, qty:int) -> float:
        customer = self.findCustomer(cname)
        customerCurrentCart = customer.CurrentCart
        unitItem = UnitItem()
        unitItem.Name = prod
        unitItem.Price = price
        unitItem.Quantity = qty
        cost = customerCurrentCart.addUnitItem(unitItem=unitItem)
        return cost

    # adds weight item to the customer's current cart and returns the cost
    def addCustWeightItem(self, cname:str, prod:str, price:float) -> float:
        customer = self.findCustomer(cname)
        weightItem = WeightItem()
        weightItem.Name = prod
        weightItem.Price = price
        cost = customer.CurrentCart.addWeightItem(weightItem=weightItem)
        return cost

    # calculates customer's current cart total
    def calcCustCartTotal(self, cname:str) -> float:
        customer = self.findCustomer(cname)
        return customer.CurrentCart.calcTotalCost()

    # adds the current cart to the customer's cart list
    def addCustCart(self, cname:str) -> None:
        pass

    # customer starts shopping with an empty cart
    def startShopping(self, cname:str) -> None:
        customer = self.findCustomer(cname)
        customer.CurrentCart = ShoppingCart()
        print(customer.CurrentCart.__dict__)

    #calculates total sales for the supermarket
    def calcTotalSales(self) -> float:
        pass

    # gets the list of customers and their transactions 
    def listCustomerTransaction(self) -> str:
        pass

    #finds customer with the most purchase
    def findTopCustomer(self) -> str:
        pass

    # calculates the customer's cart average
    def getCustAvg(self) -> float:
        pass

    # displays transaction details for a customer
    def getCustomerTransDetail(self, nm:str) -> str:
        pass

