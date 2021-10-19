#Student: Olexiy Meshechko, Student ID: 1148995

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from Supermarket import Supermarket

# HELPER FUNCTIONS


supermarket = Supermarket()
supermarket.loadCustomers()

customerNames = supermarket.getCustomerNames()


#HELPER METHODS


def getCardNumber(customerName):
    customer = supermarket.findCustomer(customerName)
    cardNumber = supermarket.getCustomerCardNumber(customer)
    cardNumberInput.configure(state='normal')
    cardNumberInput.delete(0, 'end')
    cardNumberInput.insert(0, cardNumber)
    cardNumberInput.configure(state='disabled')


def findCustomer():
    customerName = findCustomersInput.get()
    customer = supermarket.findCustomer(customerName)
    if customer:
        customersListVar.set(customer.Name)
        getCardNumber(customer.Name)
    else:
        showinfo(
        title = "Error",
        message = f"No customers found with name '{ findCustomersInput.get() }'"
    )


def showCustomerInfo():
    customerName = customersListVar.get()
    customer = supermarket.findCustomer(customerName)
    if customer:
        showinfo(
        title = "Customer Info",
        message = customer
    )
    else:
        showinfo(
        title = "Error",
        message = "Please select customer first."
    )


def startShopping():
    customerName = customersListVar.get()
    customer = supermarket.findCustomer(customerName)
    if customer:
        supermarket.startShopping(customer)
        showCurrentCart(customer)
    else:
        showinfo(
        title = "Error",
        message = "Select customer."
    )

def customerShoppingCarts():
    customerName = customersListVar.get()
    customer = supermarket.findCustomer(customerName)
    if customer:
        carts = supermarket.listCustomerCarts(customer)
        if len(carts) > 0:
            cartsStr = str(customer) + ''
            for cart in carts:
                cartsStr += str(cart) + '\n'
        else:
            cartsStr = customer + " doesn't have any carts yet."
        showinfo(
        title = customer.Name+"'s carts",
        message = cartsStr
    )
    else:
        showinfo(
        title = "Error",
        message = "Select customer."
    )



def addToCart():
    customerName = customersListVar.get()
    customer = supermarket.findCustomer(customerName)
    if customer and customer.CurrentCart:
        price = itemPriceInput.get()
        qty = itemQuantityInput.get()

        try:
            prod =  productNameInput.get()
            
            if itemTypeGroup.get() == 1: # 1 is unit item
                supermarket.addCustUnitItem(customer=customer, prod=prod, price=price, qty=qty)
            else:
                supermarket.addCustWeightItem(customer=customer, prod=prod, price=price)

            emptyProductFields()

        except ValueError as error:
            showinfo(
            title = "Error",
            message = error
        )
        showCurrentCart(customer)
        
    else:
        showinfo(
        title = "Error",
        message = "Please select customer and click 'Start shopping button'."
    )


def showCurrentCart(customer):
    cartItemsList.delete(0,'end')
    for item in customer.CurrentCart.Items:
        cartItemsList.insert(0, item)
    showCartTotal(customer)
    showCartClubPoints(customer)


def showCartTotal(customer):
    totalCostInput.configure(state='normal')
    totalCostInput.delete(0, 'end')
    totalCostInput.insert(0, supermarket.calcCustCartTotal(customer))
    totalCostInput.configure(state='disabled')


def showCartClubPoints(customer):
    currentCartClubPointsInput.configure(state='normal')
    currentCartClubPointsInput.delete(0, 'end')
    currentCartClubPointsInput.insert(0, supermarket.getCustomerCurrentCartClubPoint(customer))
    currentCartClubPointsInput.configure(state='disabled')
    

def emptyProductFields():
    productNameInput.delete(0, 'end')
    itemPriceInput.delete(0, 'end')
    itemQuantityInput.delete(0, 'end')


def checkout():
    customerName = customersListVar.get()
    customer = supermarket.findCustomer(customerName)
    if customer and customer.CurrentCart:
        if len(customer.CurrentCart.Items):
            supermarket.addCustCart(customer)
            showCurrentCart(customer)
        else:
            showinfo(
            title = "Error",
            message = "Add items to shopping cart first."
    )
    else:
        showinfo(
        title = "Error",
        message = "Please select customer and click 'Start shopping button'."
    )



# CREATE FORM
root = tk.Tk()
root.geometry("800x700")
root.resizable(False, False)
root.configure(pady="10", padx="10")
root.title('Supermarket Application')


titleLabel = tk.Label(master=root, text = "Lincoln Supermarket")  
titleLabel.configure(font=("default", 18, "bold"))
titleLabel.pack(padx=5)

# Find customer  frame
findCustomerDetailFrame = tk.LabelFrame(root, text="Find customer")
findCustomerDetailFrame.pack(ipadx=10, ipady=10, fill=tk.X, expand=True)

findCustomersInputLabel = tk.Label(master=findCustomerDetailFrame, text = "Customer Name:")  
findCustomersInputLabel.pack(padx=5, side=tk.LEFT)

findCustomersInput = tk.Entry(master=findCustomerDetailFrame, width=20)
findCustomersInput.insert(0, "")
findCustomersInput.pack(padx=5, side=tk.LEFT)


findCustomerButton = tk.Button(master=findCustomerDetailFrame, text="Find", width=20, command=findCustomer)
findCustomerButton.pack(padx=5, pady=5, side=tk.LEFT)

# Customer details frame
customerDetailFrame = tk.LabelFrame(root, text="Customer Detail")
customerDetailFrame.pack(ipadx=10, ipady=10, fill=tk.X, expand=True)

customerDetailsInputsFrame = tk.Frame(master=customerDetailFrame, relief=tk.FLAT)
customerDetailsInputsFrame.pack(ipadx=10, ipady=5, fill=tk.X, expand=True)


allCustomersLabel = tk.Label(master=customerDetailsInputsFrame, text = "Customer Name:")  
allCustomersLabel.pack(padx=5, side=tk.LEFT)


customersListVar = tk.StringVar(value=customerNames)
customersListVar.set("Select customer...") # default value
customersList = tk.OptionMenu(customerDetailsInputsFrame, customersListVar, *customerNames, command=getCardNumber)
customersList.configure(width=20)
customersList.pack(padx=5, side=tk.LEFT)

cardNumberLabel = tk.Label(master=customerDetailsInputsFrame, text = "Card Number:")  
cardNumberLabel.pack(padx=5, side=tk.LEFT)

cardNumberInput = tk.Entry(master=customerDetailsInputsFrame,state="disabled", width=20)
cardNumberInput.insert(0, "")
cardNumberInput.pack(padx=5, side=tk.LEFT)



customerDetailsButtonsFrame = tk.Frame(master=customerDetailFrame, relief=tk.FLAT, borderwidth=3)
customerDetailsButtonsFrame.pack(ipadx=10, ipady=5, fill=tk.X, expand=True)

startShoppingButton = tk.Button(master=customerDetailsButtonsFrame, text="Start Shopping", width=15, command=startShopping)
startShoppingButton.pack(padx=5, pady=5, side=tk.LEFT)

nextCustomerButton = tk.Button(master=customerDetailsButtonsFrame, text="Next Customer", width=15, command='nextCustomer')
nextCustomerButton.pack(padx=5, pady=5, side=tk.LEFT)

exitButton = tk.Button(master=customerDetailsButtonsFrame, text="Exit", width=15, command='exit')
exitButton.pack(padx=5, pady=5, side=tk.LEFT)

customerInfoButton = tk.Button(master=customerDetailsButtonsFrame, text="Customer Info", width=15, command=showCustomerInfo)
customerInfoButton.pack(padx=5, pady=5, side=tk.LEFT)

customerShoppingCarts = tk.Button(master=customerDetailsButtonsFrame, text="Customer Carts", width=15, command=customerShoppingCarts)
customerShoppingCarts.pack(padx=5, pady=5, side=tk.LEFT)

# END Customer details frame


# Transaction frame

transactionFrame = tk.LabelFrame(root, text="Transaction")
transactionFrame.pack(ipadx=20, ipady=10, fill=tk.X, expand=True)

## Product frame

productFrame = tk.Frame(master=transactionFrame, relief=tk.FLAT)
productFrame.pack(ipadx=10, ipady=5, fill=tk.X, expand=True, side=tk.LEFT)

### Product wrapper frame
productWrapperFrame = tk.Frame(master=productFrame, relief=tk.FLAT)
productWrapperFrame.pack(ipadx=10, ipady=5, fill=tk.X, expand=True, side=tk.TOP)

productLabel = tk.Label(master=productWrapperFrame, text = "Product:")  
productLabel.pack(padx=5, side=tk.LEFT)

productNameInput = tk.Entry(master=productWrapperFrame, width=20)
productNameInput.insert(0, "")
productNameInput.pack(padx=5, side=tk.LEFT)
### END Product wrapper frame

### Item type frame
def setUnitTextValues():
    if itemTypeGroup.get() == 1:
        itemQuantityPriceFrame.configure(text='Unit Item')
        itemQuantityLabel.configure(text="Number of Units")
        itemQuantityInput.configure(state='normal')
        itemPriceLabel.configure(text="Price per Unit")
    else:
        itemQuantityPriceFrame.configure(text='Weight Item')
        itemQuantityLabel.configure(text="Weight")
        itemQuantityInput.delete(0, 'end')
        itemQuantityInput.configure(state='disabled')
        itemPriceLabel.configure(text="Price per Kilo")
    emptyProductFields()


itemTypeFrame = tk.LabelFrame(productFrame, text="Item Type")
itemTypeFrame.pack(ipadx=10, ipady=10, fill=tk.X, expand=True, side=tk.TOP)

itemTypeGroup = tk.IntVar()
itemTypeGroup.set(1) # need to use v.set and v.get to
# set and get the value of this variable
unitItemRadio = tk.Radiobutton(itemTypeFrame,
                                   text="Unit Item",
                                   variable=itemTypeGroup, value=1, command=setUnitTextValues).grid(row=0, column=1)
weightItemRadio = tk.Radiobutton(itemTypeFrame,
                                   text="Weight Item",
                                   variable=itemTypeGroup, value=2, command=setUnitTextValues).grid(row=0, column=2)

### END Item type frame

### Item price frame


itemQuantityPriceFrame = tk.LabelFrame(productFrame, text="Unit Item")
itemQuantityPriceFrame.pack(ipadx=10, ipady=10, fill=tk.X, expand=True, side=tk.TOP)


#### Item quantity wrapper frame
itemQuantityWrapperFrame = tk.Frame(master=itemQuantityPriceFrame, relief=tk.FLAT)
itemQuantityWrapperFrame.pack(ipadx=10, ipady=5, fill=tk.X, expand=True, side=tk.TOP)


itemQuantityLabel = tk.Label(master=itemQuantityWrapperFrame, text = "Number of Units", width=20)  
itemQuantityLabel.pack(padx=5, side=tk.LEFT)

itemQuantityData = tk.IntVar()
itemQuantityInput = tk.Entry(textvariable=itemQuantityData,master=itemQuantityWrapperFrame, width=20)
itemQuantityInput.insert(0, "")
itemQuantityInput.pack(padx=5, side=tk.LEFT)
#### END Item quantity wrapper frame

#### Item price wrapper frame
itemPriceWrapperFrame = tk.Frame(master=itemQuantityPriceFrame, relief=tk.FLAT)
itemPriceWrapperFrame.pack(ipadx=10, ipady=5, fill=tk.X, expand=True, side=tk.TOP)


itemPriceLabel = tk.Label(master=itemPriceWrapperFrame, text = "Price per Unit", width=20)  
itemPriceLabel.pack(padx=5, side=tk.LEFT)

itemPriceData = tk.DoubleVar()
itemPriceInput = tk.Entry(textvariable=itemPriceData,master=itemPriceWrapperFrame, width=20)
itemPriceInput.insert(0, "")
itemPriceInput.pack(padx=5, side=tk.LEFT)
#### END Item price wrapper frame



## END Product frame

## Cart frame
cartFrame = tk.Frame(master=transactionFrame, relief=tk.FLAT)
cartFrame.pack(ipadx=10, ipady=5, fill=tk.X, expand=True)

### Cart and buttons frame
cartItemsList = tk.Listbox(master=cartFrame, exportselection=False)
cartItemsList.pack(padx=5, pady=5, fill=tk.X)

addToCartButton = tk.Button(master=cartFrame, text="Add to Cart", width=10, command=addToCart)
addToCartButton.pack(padx=5, pady=5, side=tk.LEFT)

newItemButton = tk.Button(master=cartFrame, text="New Item", width=10, command=emptyProductFields)
newItemButton.pack(padx=5, pady=5, side=tk.LEFT)

checkoutButton = tk.Button(master=cartFrame, text="Checkout", width=10, command=checkout)
checkoutButton.pack(padx=5, pady=5, side=tk.LEFT)
### END Cart and buttons frame

### Total cost frame
totalCostFrame = tk.Frame(master=transactionFrame, relief=tk.FLAT)
totalCostFrame.pack(ipadx=10, ipady=5, fill=tk.X, expand=True)

totalCostLabel = tk.Label(master=totalCostFrame, text = "Total Cost:")  
totalCostLabel.pack(padx=5, side=tk.LEFT)

totalCostInput = tk.Entry(master=totalCostFrame, width=20, state='disabled')
totalCostInput.insert(0, "")
totalCostInput.pack(padx=5, side=tk.LEFT)
### END Total cost frame

### Current cart club points frame
currentCartClubPointsFrame = tk.Frame(master=transactionFrame, relief=tk.FLAT)
currentCartClubPointsFrame.pack(ipadx=10, ipady=5, fill=tk.X, expand=True)

currentCartClubPointsLabel = tk.Label(master=currentCartClubPointsFrame, text = "Current Cart Club Points:")  
currentCartClubPointsLabel.pack(padx=5, side=tk.LEFT)

currentCartClubPointsInput = tk.Entry(master=currentCartClubPointsFrame, width=10, state='disabled')
currentCartClubPointsInput.insert(0, "")
currentCartClubPointsInput.pack(padx=5, side=tk.LEFT)
#### END Current cart club points frame
## END Cart frame
# END Transaction frame


# Summary frame
summaryFrame = tk.LabelFrame(root, text="Summary")
summaryFrame.pack(ipadx=10, ipady=10, fill=tk.X, expand=True)

salesByCustomerButton = tk.Button(master=summaryFrame, text="Sales by Customer", width=20, command='salesByCustomer')
salesByCustomerButton.pack(padx=5, pady=5, side=tk.LEFT)

totalSalesButton = tk.Button(master=summaryFrame, text="Total Sales", width=20, command='totalSales')
totalSalesButton.pack(padx=5, pady=5, side=tk.LEFT)

topCustomerButton = tk.Button(master=summaryFrame, text="Top Customer", width=20, command='topCustomer')
topCustomerButton.pack(padx=5, pady=5, side=tk.LEFT)

averageCartButton = tk.Button(master=summaryFrame, text="Average Cart", width=20, command='averageCart')
averageCartButton.pack(padx=5, pady=5, side=tk.LEFT)
#END Summary frame

# # frame with a list of customers
# customersFrame = ttk.Frame(relief=tk.FLAT, borderwidth=3)
# customersFrame.pack(ipadx=10, ipady=5, fill='y', expand=True, side=tk.LEFT)

# allCustomersLabel = ttk.Label(master=customersFrame, text = "Customers")  
# allCustomersLabel.pack() 

# allCustomersList = tk.Listbox(master=customersFrame, exportselection=False)  

# allCustomersList.pack(fill='x')

# # rent movie button
# rentButton  = ttk.Button(master=customersFrame, text="Rent", command='rentMovie')
# rentButton.pack(padx=5, pady=5, side=tk.RIGHT)

# # customer detail button
# customerDetailsButton  = ttk.Button(master=customersFrame, text="Customer detail", command='showCustomerDetail')
# customerDetailsButton.pack(padx=5, pady=5, side=tk.LEFT)



# # frame with a list of movies
# moviesFrame = ttk.Frame(relief=tk.FLAT, borderwidth=3)
# moviesFrame.pack(ipadx=10, ipady=5, fill='y', expand=True, side=tk.RIGHT)

# allMoviesLabel = ttk.Label(master=moviesFrame, text = "Movies")  
# allMoviesLabel.pack() 

# allMoviesList = tk.Listbox(master=moviesFrame, exportselection=False)  

# allMoviesList.pack(fill='x')

# # return movie button
# returnButton  = ttk.Button(master=moviesFrame, text="Return", command='returnMovie')
# returnButton.pack(padx=5, pady=5, side=tk.LEFT)

# # movie detail button
# movieDetailsButton = ttk.Button(master=moviesFrame, text="Movie detail", command='showMovieDetail')
# movieDetailsButton.pack(padx=5, pady=5, side=tk.RIGHT)

root.mainloop()