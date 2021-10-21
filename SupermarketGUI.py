#Student: Olexiy Meshechko, Student ID: 1148995

import tkinter as tk
from tkinter.messagebox import showinfo
from Supermarket import Supermarket

# HELPER FUNCTIONS
supermarket = Supermarket()
supermarket.loadCustomers()
customerNames = supermarket.getCustomerNames()

# create modal
def showSimpleModal(title:str, text:str):
    modal = tk.Toplevel(root)
    modal.geometry("600x300")
    modal.configure(pady="10", padx="10")
    modal.title(title)
    modalHeaderLbel = tk.Label(modal, text = title, anchor="nw", justify = 'left', width=500)
    modalHeaderLbel.configure(font=("default", 18, "bold"))
    modalHeaderLbel.pack(fill="x")
    modalLabel = tk.Label(modal, text = text, anchor="nw", justify = 'left', width=500)
    modalLabel.pack(fill="x")


def findCustomer():
    customerName = findCustomersInput.get()
    if customerName:
        customer = supermarket.findCustomer(customerName)
        if customer:
            customersListVar.set(supermarket.getCustomerName(customer))
            startShopping(supermarket.getCustomerName(customer))
        else:
            showinfo(
            title = "Error",
            message = f"No customers found with name '{ findCustomersInput.get() }'"
        )
    else:
        showinfo(
            title = "Error",
            message = "Enter customer name."
        )


def startShopping(customerName):
    customer = supermarket.findCustomer(customerName)
    if customer:
        cardNumber = supermarket.getCustomerCardNumber(customer)
        cardNumberInput.configure(state='normal')
        cardNumberInput.delete(0, 'end')
        cardNumberInput.insert(0, cardNumber)
        cardNumberInput.configure(state='disabled')
        supermarket.startShopping(customer)
        emptyProductFields()
        showCurrentCart(customer)
    else:
        showinfo(
        title = "Error",
        message = "Select customer."
    )


def showCurrentCart(customer):
    cartItemsList.delete(0,'end')
    for item in supermarket.customerCurrentCartItems(customer):
        cartItemsList.insert(0, item)
    showCartTotal(customer)
    showCartClubPoints(customer)


def showCustomerInfo():
    customerName = customersListVar.get()
    customer = supermarket.findCustomer(customerName)
    if customer:
        cstomerTransactions = supermarket.getCustomerTransDetail(customer)
        showSimpleModal(title="Customer info", text=cstomerTransactions)
        
    else:
        showinfo(
        title = "Error",
        message = "Select customer."
    )


# update labels on item type change
def setUnitTypeFrameTextValues():
    if itemTypeGroup.get() == 1:
        itemPriceQuantityFrame.configure(text='Unit Item')
        itemQuantityLabel.configure(text="Number of Units")
        itemQuantityInput.configure(state='normal')
        itemPriceLabel.configure(text="Price per Unit")
    else:
        itemPriceQuantityFrame.configure(text='Weight Item')
        itemQuantityLabel.configure(text="Weight")
        itemQuantityInput.delete(0, 'end')
        itemQuantityInput.configure(state='disabled')
        itemPriceLabel.configure(text="Price per Kilo")
    emptyProductFields()


def addToCart():
    customerName = customersListVar.get()
    customer = supermarket.findCustomer(customerName)
    if customer:
        price = itemPriceInput.get()
        qty = itemQuantityInput.get()
        try:
            prod = itemNameInput.get()
            if itemTypeGroup.get() == 1: # 1 is unit item
                supermarket.addCustUnitItem(customer=customer, prod=prod, price=price, qty=qty)
            else:
                supermarket.addCustWeightItem(customer=customer, prod=prod, price=price)
            emptyProductFields()

        except ValueError as error:  # validate product name, price or quantity fields and show error if invalif data was entered 
            showinfo(
            title = "Error",
            message = error
        )
        showCurrentCart(customer)
    else:
        showinfo(
        title = "Error",
        message = "Select customer."
    )


def emptyProductFields():
    itemNameInput.delete(0, 'end')
    itemPriceInput.delete(0, 'end')
    itemQuantityInput.delete(0, 'end')


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


def checkout():
    customerName = customersListVar.get()
    customer = supermarket.findCustomer(customerName)
    if customer:
        if len(supermarket.customerCurrentCartItems(customer)): #check if some items were addedd to customer cart
            supermarket.addCustCart(customer) 
            showinfo(
            title = "Transaction completed",
            message = f"Transaction completed. Total paid: ${ supermarket.calcCustCartTotal(customer) }. Club points earned: { supermarket.getCustomerCurrentCartClubPoint(customer) }."
            )
            supermarket.startShopping(customer) # empty cstomer cart 
            showCurrentCart(customer) # empty cartlist 
        else:
            showinfo(
            title = "Error",
            message = "Add items to shopping cart first."
            )
    else:
        showinfo(
        title = "Error",
        message = "Select customer."
        )


def salesByCustomer():
    showSimpleModal(title="Summary of all the sales.", text=supermarket.getAllCustomersTransSummary())
    

def totalSales():
    title = "Total sales"
    modal = tk.Toplevel(root)
    modal.geometry("600x300")
    modal.configure(pady="10", padx="10")
    modal.title(title)

    modalHeaderLbel = tk.Label(modal, text = title, anchor="nw", justify = 'left', width=500)
    modalHeaderLbel.configure(font=("default", 18, "bold"))
    modalHeaderLbel.pack(fill="x")

    salesLabelFrame = tk.LabelFrame(master=modal, relief=tk.FLAT)
    salesLabelFrame.pack(padx=10, pady=10,  expand=True, side=tk.RIGHT, anchor="nw",)

    salesLabel = tk.Label(salesLabelFrame, anchor="nw", justify = 'left')
    salesLabel.pack(fill="x")

    def getSalesByPeriod(period):
        salesLabel.config(text=supermarket.calcTotalSales(period = period))

    salesPeriodFrame = tk.LabelFrame(master=modal, relief=tk.FLAT)
    salesPeriodFrame.pack(padx=10, pady=10, expand=True, side=tk.LEFT, anchor="nw")

    salesPeriods = ["Sales to date", "Current year", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    salesPeriodListVar = tk.StringVar(value=salesPeriods)
    salesPeriodListVar.set("Sales to date") # default value
    salesPeriodList = tk.OptionMenu(salesPeriodFrame, salesPeriodListVar, *salesPeriods, command=getSalesByPeriod)
    salesPeriodList.configure(width=20)
    salesPeriodList.pack(padx=5)

    getSalesByPeriod(period="Sales to date")


def topCustomer():
    showSimpleModal(title="Top 3 customers with the largest purchase total.", text=supermarket.findTopCustomer())


def averageCart():
    showSimpleModal(title="Average spending of each customer per transaction.", text=supermarket.getCustAvg())
    

# CREATE FORM
root = tk.Tk()
root.geometry("800x700")
root.resizable(False, False)
root.configure(pady="10", padx="10")
root.title('Supermarket Application')
titleLabel = tk.Label(master=root, text = "Lincoln Supermarket")  
titleLabel.configure(font=("default", 18, "bold"))
titleLabel.pack(padx=5)

# Find customer frame
findCustomerDetailFrame = tk.LabelFrame(root, text=f"Find customer (total customers: {str(supermarket.countCustomers())})")
findCustomerDetailFrame.pack(ipadx=10, ipady=10, fill=tk.X, expand=True)

findCustomersInputLabel = tk.Label(master=findCustomerDetailFrame, text = "Customer Name:")  
findCustomersInputLabel.pack(padx=5, side=tk.LEFT)

findCustomersInput = tk.Entry(master=findCustomerDetailFrame, width=20)
findCustomersInput.insert(0, "")
findCustomersInput.pack(padx=5, side=tk.LEFT)

findCustomerButton = tk.Button(master=findCustomerDetailFrame, text="Find", width=20, command=findCustomer)
findCustomerButton.pack(padx=5, pady=5, side=tk.LEFT)
# ED Find customer frame

# Customer details frame
customerDetailFrame = tk.LabelFrame(root, text="Customer Detail.")
customerDetailFrame.pack(ipadx=10, ipady=10, fill=tk.X, expand=True)

customerDetailsInputsFrame = tk.Frame(master=customerDetailFrame, relief=tk.FLAT)
customerDetailsInputsFrame.pack(ipadx=10, ipady=5, fill=tk.X, expand=True)

allCustomersLabel = tk.Label(master=customerDetailsInputsFrame, text = "Customer Name:")  
allCustomersLabel.pack(padx=5, side=tk.LEFT)

customersListVar = tk.StringVar(value=customerNames)
customersListVar.set("Select customer...") # default value
customersList = tk.OptionMenu(customerDetailsInputsFrame, customersListVar, *customerNames, command=startShopping)
customersList.configure(width=20)
customersList.pack(padx=5, side=tk.LEFT)

cardNumberLabel = tk.Label(master=customerDetailsInputsFrame, text = "Card Number:")  
cardNumberLabel.pack(padx=5, side=tk.LEFT)

cardNumberInput = tk.Entry(master=customerDetailsInputsFrame,state="disabled", width=20)
cardNumberInput.insert(0, "")
cardNumberInput.pack(padx=5, side=tk.LEFT)

customerInfoButton = tk.Button(master=customerDetailsInputsFrame, text="Customer Info", width=20, command=showCustomerInfo)
customerInfoButton.pack(padx=5, pady=5, side=tk.LEFT)
# END Customer details frame


# Transaction frame
transactionFrame = tk.LabelFrame(root, text="Transaction")
transactionFrame.pack(ipadx=10, ipady=10, fill=tk.X, expand=True)

## Item frame
itemFrame = tk.Frame(master=transactionFrame, relief=tk.FLAT)
itemFrame.pack(padx=10, pady=10, fill=tk.X, expand=True, side=tk.LEFT, anchor="nw",)

### Item type frame
itemTypeFrame = tk.LabelFrame(itemFrame, text="Item Type")
itemTypeFrame.pack(ipadx=10, ipady=10, fill=tk.X, expand=True, side=tk.TOP)

itemTypeGroup = tk.IntVar()
itemTypeGroup.set(1)
unitItemRadio = tk.Radiobutton(itemTypeFrame,
                                   text="Unit Item",
                                   variable=itemTypeGroup, value=1, command=setUnitTypeFrameTextValues).grid(row=0, column=1)
weightItemRadio = tk.Radiobutton(itemTypeFrame,
                                   text="Weight Item",
                                   variable=itemTypeGroup, value=2, command=setUnitTypeFrameTextValues).grid(row=0, column=2)
### END Item type frame

### Item name frame
itemNameFrame = tk.Frame(master=itemFrame, relief=tk.FLAT)
itemNameFrame.pack(ipadx=10, ipady=10, fill=tk.X, expand=True, side=tk.TOP)

itemLabel = tk.Label(master=itemNameFrame, text = "Product:")  
itemLabel.pack(padx=5, side=tk.LEFT)

itemNameInput = tk.Entry(master=itemNameFrame, width=20)
itemNameInput.insert(0, "")
itemNameInput.pack(padx=5, side=tk.LEFT)
### END Item name frame

### Item price/quantity frame
itemPriceQuantityFrame = tk.LabelFrame(itemFrame, text="Unit Item")
itemPriceQuantityFrame.pack(ipadx=10, ipady=10, fill=tk.X, expand=True, side=tk.TOP)


#### Item quantity frame
itemQuantityFrame = tk.Frame(master=itemPriceQuantityFrame, relief=tk.FLAT)
itemQuantityFrame.pack(ipadx=10, ipady=5, fill=tk.X, expand=True, side=tk.TOP)

itemQuantityLabel = tk.Label(master=itemQuantityFrame, text = "Number of Units", width=20)  
itemQuantityLabel.pack(padx=5, side=tk.LEFT)

itemQuantityData = tk.IntVar()
itemQuantityInput = tk.Entry(textvariable=itemQuantityData,master=itemQuantityFrame, width=20)
itemQuantityInput.insert(0, "")
itemQuantityInput.pack(padx=5, side=tk.LEFT)
#### END Item quantity frame

#### Item price frame
itemPriceFrame = tk.Frame(master=itemPriceQuantityFrame, relief=tk.FLAT)
itemPriceFrame.pack(ipadx=10, ipady=5, fill=tk.X, expand=True, side=tk.TOP)

itemPriceLabel = tk.Label(master=itemPriceFrame, text = "Price per Unit", width=20)  
itemPriceLabel.pack(padx=5, side=tk.LEFT)

itemPriceData = tk.DoubleVar()
itemPriceInput = tk.Entry(textvariable=itemPriceData,master=itemPriceFrame, width=20)
itemPriceInput.insert(0, "")
itemPriceInput.pack(padx=5, side=tk.LEFT)
#### END Item price frame

### Item buttons frame
itemButtonsFrame = tk.Frame(master=itemFrame, relief=tk.FLAT)
itemButtonsFrame.pack(ipadx=10, ipady=5, fill=tk.X, expand=True)

addToCartButton = tk.Button(master=itemButtonsFrame, text="Add to Cart", width=10, command=addToCart)
addToCartButton.pack(padx=5, pady=5, side=tk.RIGHT, anchor="e")

newItemButton = tk.Button(master=itemButtonsFrame, text="New Item", width=10, command=emptyProductFields)
newItemButton.pack(padx=5, pady=5, side=tk.RIGHT, anchor="e")
### END Item buttons frame
## END Product frame

## Cart frame
cartFrame = tk.LabelFrame(master=transactionFrame, text="Cart")
cartFrame.pack(padx=10, pady=0, fill=tk.X, expand=True)

### Cart details frame
cartDetailsFrame = tk.Frame(master=cartFrame, relief=tk.FLAT)
cartDetailsFrame.pack(padx=10, pady=5, fill=tk.X, expand=True)

cartItemsList = tk.Listbox(master=cartDetailsFrame, exportselection=False)
cartItemsList.pack(padx=5, pady=5, fill=tk.X)

#### Total cost frame
totalCostFrame = tk.Frame(master=cartFrame, relief=tk.FLAT)
totalCostFrame.pack(padx=10, pady=5, fill=tk.X, expand=True)

totalCostLabel = tk.Label(master=totalCostFrame, text = "Total Cost:")  
totalCostLabel.pack(padx=5, side=tk.LEFT)

totalCostInput = tk.Entry(master=totalCostFrame, width=20, state='disabled')
totalCostInput.insert(0, "")
totalCostInput.pack(padx=5, side=tk.LEFT)
#### END Total cost frame

#### Current cart club points frame
currentCartClubPointsFrame = tk.Frame(master=cartFrame, relief=tk.FLAT)
currentCartClubPointsFrame.pack(padx=10, pady=5, fill=tk.X, expand=True)

currentCartClubPointsLabel = tk.Label(master=currentCartClubPointsFrame, text = "Current Cart Club Points:")  
currentCartClubPointsLabel.pack(padx=5, side=tk.LEFT)

currentCartClubPointsInput = tk.Entry(master=currentCartClubPointsFrame, width=10, state='disabled')
currentCartClubPointsInput.insert(0, "")
currentCartClubPointsInput.pack(padx=5, side=tk.LEFT)
#### END Current cart club points frame

checkoutButton = tk.Button(master=cartFrame, text="Checkout", width=20, command=checkout)
checkoutButton.pack(padx=10, pady=20, fill=tk.X, anchor="e")
### END Cart details frame
## END Cart frame
# END Transaction frame


# Summary frame
summaryFrame = tk.LabelFrame(root, text="Summary")
summaryFrame.pack(ipadx=10, ipady=10, fill=tk.X, expand=True)

salesByCustomerButton = tk.Button(master=summaryFrame, text="Sales by Customer", width=20, command=salesByCustomer)
salesByCustomerButton.pack(padx=5, pady=5, side=tk.LEFT)

totalSalesButton = tk.Button(master=summaryFrame, text="Total Sales", width=20, command=totalSales)
totalSalesButton.pack(padx=5, pady=5, side=tk.LEFT)

topCustomerButton = tk.Button(master=summaryFrame, text="Top Customers", width=20, command=topCustomer)
topCustomerButton.pack(padx=5, pady=5, side=tk.LEFT)

averageCartButton = tk.Button(master=summaryFrame, text="Average Cart", width=20, command=averageCart)
averageCartButton.pack(padx=5, pady=5, side=tk.LEFT)
#END Summary frame

root.mainloop()