from UnitItem import UnitItem
from WeightItem import WeightItem
from ShoppingCart import ShoppingCart
from Customer import Customer
import pytest

unitItem_1 = UnitItem()
unitItem_1.Name = 'Juice'
unitItem_1.Price = 1
unitItem_1.Quantity = 5

unitItem_2 = UnitItem()
unitItem_2.Name = 'Bread'
unitItem_2.Price = 2
unitItem_2.Quantity = 10

weightItem_1 = WeightItem()
weightItem_1.Name = 'Tomato'
weightItem_1.ProductWeight = 3
weightItem_1.Price = 10

weightItem_2 = WeightItem()
weightItem_2.Name = 'Cucumber'
weightItem_2.ProductWeight = 5
weightItem_2.Price = 20

items = [unitItem_1, unitItem_2, weightItem_1, weightItem_2]

cart = ShoppingCart()
cart.addUnitItem(unitItem_1)
cart.addUnitItem(unitItem_2)
cart.addUnitItem(weightItem_1)
cart.addUnitItem(weightItem_2)

@pytest.fixture(scope='module')
def customer():
    customer = Customer('John Smith')
    customer.CurrentCart = cart
    return customer

def test_calcClubPoint(customer):
    assert customer.calcClubPoint() == 15

def test_addToCartList(customer):
    customer.addToCartList()
    assert len(customer.CartList) == 1
    customer.CurrentCart == ShoppingCart()
    customerCarts = customer.CartList
    assert 'Tomato' in str(customerCarts[0])

def test_updateTotal(customer):
    customer.updateTotal()
    assert customer.TotalToDate == 155

def test_updateClubPoint(customer):
    customer.updateClubPoint()
    assert customer.ClubPoint == 15

def test_custStr(customer):
    assert 'John' in str(customer)

def test_custTrans(customer):
    assert '155' in customer.custTrans()

def test_custDetailTrans(customer):
    assert 'Tomato' in customer.custDetailTrans()

def test_cartAverage(customer):
    assert customer.cartAverage() == 155