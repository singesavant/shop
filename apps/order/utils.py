import random
from datetime import datetime

from oscar.apps.order.utils import OrderNumberGenerator as CoreOrderNumberGenerator


class OrderNumberGenerator(CoreOrderNumberGenerator):
    def order_number(self, basket):
        monkey_species = ['BABOON', 'MONKEY', 'APE', 'GORILLA', 'CAPUCHIN', 'TAMARIN', 'GIBBON']
        specie = random.choice(monkey_species)
        num = 'WEB{0}-{1}-{2}'.format(specie,
                                      datetime.strftime(datetime.now(), '%Y%m%d'),
                                      42 + basket.id)
        return num
