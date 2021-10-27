from UnitItem import UnitItem
from WeightItem import WeightItem
from ShoppingCart import ShoppingCart
from datetime import datetime
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


@pytest.fixture(scope='module')
def cart():
    cart = ShoppingCart()
    return cart

def test_date(cart):
    assert cart.PurchaseDate.date() == datetime.now().date()

def test_addUnitItem(cart):
    assert cart.addUnitItem(unitItem_1) == 5
    assert cart.addUnitItem(unitItem_2) == 20
    assert len(cart.Items) == 2

def test_addWeightItem(cart):
    assert cart.addWeightItem(weightItem_1) == 30
    assert cart.addWeightItem(weightItem_2) == 100
    assert len(cart.Items) == 4

def test_calcTotalCost(cart):
    assert cart.calcTotalCost() == 155

def test_cartStr(cart):
    assert 'Bread' in str(cart)
