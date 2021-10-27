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
weightItem_1.Price = 10

weightItem_2 = WeightItem()
weightItem_2.Name = 'Cucumber'
weightItem_2.Price = 20


@pytest.fixture(scope='module')
def cart():
    cart = ShoppingCart()
    return cart

# this always fails as there's a couple ms difference between object creation and text excution
# def test_date(cart):
#     assert cart.PurchaseDate == datetime.now()

def test_addUnitItem(cart):
    assert cart.addUnitItem(unitItem_1) == 5
    assert cart.addUnitItem(unitItem_2) == 20
    assert len(cart.Items) == 2

def test_addWeightItem(cart):
    assert cart.addWeightItem(weightItem_1) == weightItem_1.calcCost()
    assert cart.addWeightItem(weightItem_2) == weightItem_2.calcCost()
    assert len(cart.Items) == 4

def test_calcTotalCost(cart):
    total = 25 + weightItem_1.calcCost() + weightItem_2.calcCost()
    assert cart.calcTotalCost() == total

def test_cartStr(cart):
    total = 25 + weightItem_1.calcCost() + weightItem_2.calcCost()
    reqStr = f'\n27/10/2021 ${total} \nJuice: $1.0 x 5 = $5.0\nBread: $2.0 x 10 = $20.0\nTomato: $10.0 x {weightItem_1.ProductWeight}kg = ${weightItem_1.calcCost()}\nCucumber: $20.0 x {weightItem_2.ProductWeight}kg = ${weightItem_2.calcCost()}'
    assert str(cart) == reqStr