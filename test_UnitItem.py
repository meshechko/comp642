from UnitItem import UnitItem
from contextlib import contextmanager
import pytest

@contextmanager
def does_not_raise():
    yield


@pytest.fixture(scope='module')
def item():
    item = UnitItem()
    return item


def test_name(item):
    item.Name = 'Juice'
    assert item.Name == 'Juice'

    valueErrorStr = 'Incorrect value: product name.'
    with pytest.raises(ValueError, match=valueErrorStr):
        item.Name = ''

@pytest.mark.parametrize(
    "input,expectation",
    [
        (6, does_not_raise()),
        ('', pytest.raises(ValueError)),
        ('string value', pytest.raises(ValueError)),
        (-6.1, pytest.raises(ValueError)),
        (0, pytest.raises(ValueError)),
    ],
)
def test_quantity(item, input, expectation):
    with expectation:
        item.Quantity = input
        assert item.Quantity is not None


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
    item.Quantity = 6
    item.Price = 1.50
    assert item.calcCost() == 9.00


def test_itemStr(item):
    item.Name = 'Juice'
    item.Quantity = 4
    item.Price = 1.5
    assert 'Juice' in str(item)


