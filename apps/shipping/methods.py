from decimal import Decimal as D

from oscar.apps.shipping import methods
from oscar.core import prices

class Pickup(methods.Base):
    code = 'pickup'
    name = 'Pickup (free)'

    def calculate(self, basket):
        return prices.Price(
            currency=basket.currency,
            excl_tax=D('0.00'), incl_tax=D('0.00'))
