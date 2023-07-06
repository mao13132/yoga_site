import json
from yookassa import Configuration, Payment
from .settings import SHOP_ID, PAYMENT_TOKEN


class Ukassa:
    def __init__(self):
        Configuration.account_id = SHOP_ID
        Configuration.secret_key = PAYMENT_TOKEN

    def create_payment(self, target_price, discript, link):
        payment = Payment.create({
            "amount": {
                "value": target_price,
                "currency": "RUB"
            },
            "payment_method_data": {
                "type": "bank_card"
            },
            "confirmation": {
                "type": "redirect",
                "return_url": link
            },
            "capture": True,
            "description": discript
        })

        payment_data = json.loads(payment.json())
        payment_id = payment_data['id']
        payment_url = (payment_data['confirmation'])['confirmation_url']

        return payment_url
