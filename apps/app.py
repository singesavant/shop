from oscar.app import Shop

from apps.checkout.app import application as checkout_app


class SingeSavantShop(Shop):
    checkout_app = checkout_app


application = SingeSavantShop()
