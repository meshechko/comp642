from WeightItem import WeightItem
from contextlib import contextmanager
import pytest


@contextmanager
def does_not_raise():
    yield


@pytest.fixture(scope='module')
def item():
    item = WeightItem()
    return item


def test_name(item):
    item.Name = 'Tomato'
    assert item.Name == 'Tomato'

    valueErrorStr = 'Incorrect value: product name.'
    with pytest.raises(ValueError, match=valueErrorStr):
        item.Name = ''


def test_scale(item):
    assert  isinstance(item.scale(), float)
    assert item.scale() >= 0 and item.scale() < 4
    assert item.scale() >= 0 and item.scale() < 4
    assert item.scale() >= 0 and item.scale() < 4
    assert item.scale() >= 0 and item.scale() < 4


@pytest.mark.parametrize(
    "input,expectation",
    [
        (6.1, does_not_raise()),
        ('', pytest.raises(ValueError)),
        ('string value', pytest.raises(ValueError)),
        (-6.1, pytest.raises(ValueError)),
        (0, pytest.raises(ValueError)),
    ],
)
def test_price(item, input, expectation):
    with expectation:
        item.Price = input
        assert item.Price is not None

def test_calcCost(item):
    price = 1.50
    item.Price = price
    cost = float(format(price * item.ProductWeight, '.2f'))
    assert item.calcCost() == cost


def test_itemStr(item):
    item.Name = 'Tomato'
    weight = item.ProductWeight
    price = 1.5
    item.Price = price
    cost = float(format(price * weight, '.2f'))
    assert str(item) == f'Tomato: $1.5 x {weight}kg = ${cost}'



