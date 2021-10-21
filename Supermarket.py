#Student: Olexiy Meshechko, Student ID: 1148995

from Customer import Customer
from ShoppingCart import ShoppingCart
from Item import Item
from UnitItem import UnitItem
from WeightItem import WeightItem
from typing import List
from datetime import datetime

class Supermarket:
    #constructor
    def __init__(self) -> None:
        self.__customers: List[Customer] = []


    #getter for the list of customers
    @property 
    def CustomerList(self) -> List[Customer]:
        return self.__customers


    def getCustomerNames(self) -> List[str]:
        names = []
        for customer in self.__customers:
            names.append(customer.Name)
        return names


     # read customers from txt
    def loadCustomers(self) -> None:
        with open('Customers.txt', 'r') as f: 
            lines = f.readlines()
            for line in lines:
                data = line.split(',')
                name = data[0]
                self.addCustomer(name.strip())


    #creates and adds new customer to the customer list
    def addCustomer(self, name:str) -> None:
        self.__customers.append(Customer(name))


    # finds a customer object based on a customer's name
    def findCustomer(self, cname:str) -> Customer:
        for customer in self.__customers:
            if cname.lower() in customer.Name.lower():
                return customer
                
    def countCustomers(self):
        return len(self.CustomerList)

    def getCustomerName(self, customer:Customer) -> str:
        name = customer.Name
        return name

    # finds a customer's card number based on a customer's name
    def getCustomerCardNumber(self, customer:Customer) -> int:
        return customer.CardNumber


    # gets the club point for a current customer 
    def getCustomerClubPoint(self, customer:Customer) -> int:
        return customer.ClubPoint
    

    # gets the club point for customer current cart
    def getCustomerCurrentCartClubPoint(self, customer:Customer) -> int:
        return customer.calcClubPoint()


    # adds unit item to the customer's current cart and returns the cost
    def addCustUnitItem(self, customer:Customer, prod:str, price:float, qty:int) -> float:
        customerCurrentCart = customer.CurrentCart
        unitItem = UnitItem()
        unitItem.Name = prod
        unitItem.Price = price
        unitItem.Quantity = qty
        cost = customerCurrentCart.addUnitItem(unitItem=unitItem)
        return cost


    # adds weight item to the customer's current cart and returns the cost
    def addCustWeightItem(self, customer:Customer, prod:str, price:float) -> float:
        weightItem = WeightItem()
        weightItem.Name = prod
        weightItem.Price = price
        cost = customer.CurrentCart.addWeightItem(weightItem=weightItem)
        return cost


    # calculates customer's current cart total
    def calcCustCartTotal(self, customer:Customer) -> float:
        return customer.CurrentCart.calcTotalCost()

    # adds the current cart to the customer's cart list
    def addCustCart(self, customer:Customer) -> None:
        # Update customer club points
        customer.updateClubPoint()
        # Update custome todate spent
        customer.updateTotal()
        # Move current cart to list of all carts
        customer.addToCartList()
        # Empty customer current cart

    # customer starts shopping with an empty cart
    def startShopping(self, customer:Customer) -> None:
        customer.CurrentCart = ShoppingCart()


    #calculates total sales for the supermarket
    def calcTotalSales(self, period:str) -> str:
        currentYear = datetime.now().strftime("%Y")
        reportStr = f"Sales for '{ period }'{chr(10)}{chr(10)}"
        grandTotal = 0
        for customer in self.__customers:
            customerStr = ''
            customerTotal = 0
            for cart in self.listCustomerCarts(customer):
                purchaseDate = cart.PurchaseDate.strftime('%B') 
                purchaseYear = cart.PurchaseDate.strftime('%Y')
                if period == "Sales to date":
                    customerTotal += cart.calcTotalCost()
                elif period == "Current year":
                    if purchaseYear == currentYear:
                        customerTotal += cart.calcTotalCost()
                else:
                    if purchaseDate == period and purchaseYear == currentYear:
                        customerTotal += cart.calcTotalCost()
            grandTotal += customerTotal
            if customerTotal:
                customerStr += f'{ customer.Name } { customer.CardNumber } ${ customerTotal }{chr(10)}'
            reportStr += customerStr
        reportStr += f"{chr(10)}Total: ${ float(format(grandTotal, '.2f')) }"
        return reportStr


    # gets the list of customer transactions 
    def listCustomerCarts(self, customer:Customer) -> List[ShoppingCart]:
        return customer.CartList

    def customerCurrentCartItems(self, customer:Customer) -> List[Item]:
        return customer.CurrentCart.Items

    #finds 3 customer with the most purchase
    def findTopCustomer(self) -> str:
        customers = [customer for customer in self.__customers if customer.TotalToDate > 0]
        customers.sort(key=lambda customer: customer.TotalToDate, reverse=True)
        customersStr = ''
        if len(customers):
            i = 1
            for customer in customers[:3]:
                customersStr += f'{i}. {str(customer)}{chr(10)}'
                i += 1
        else:
            customersStr = 'No customers shopped at the supermarket yet.'
        return customersStr
            

    # returns customers cart average
    def getCustAvg(self) -> str:
        averageStr = ''
        countCustomerPurchases = 0
        for customer in self.__customers:
            if customer.TotalToDate:
                averageStr += f'{ customer.Name } ${ customer.cartAverage() }{chr(10)}'
                countCustomerPurchases += 1

        if countCustomerPurchases == 0:
            averageStr = 'No customers shopped at the supermarket yet.'
        return averageStr


    # displays transaction details for a customer
    def getCustomerTransDetail(self, customer:Customer) -> str:
        return customer.custDetailTrans()


    def getAllCustomersTransSummary(self)-> str:
        transStr = ''
        countCustomerPurchases = 0
        for customer in self.__customers:
            if customer.TotalToDate:
                transStr += customer.custTrans()
                countCustomerPurchases += 1
        if countCustomerPurchases == 0:
            transStr = 'No customers shopped at the supermarket yet.'
        return transStr


