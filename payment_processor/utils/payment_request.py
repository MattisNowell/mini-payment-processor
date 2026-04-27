from django.http import HttpRequest
from decimal import Decimal

class PaymentRequest:
    
    valid_currencies = ('USD',
                        'GBP',
                        'EUR',
                        'CAD')
    
    valid_payment_methods = ('paypal',
                    'klana',
                    'mastercard',
                    'visa',
                    'amex')
  
    def __init__(self, request:HttpRequest):
        self._data = request 
    
        if not isinstance(self._data['amount'], (Decimal, int, float)):
            raise TypeError("Payment amount must be a value of type int, float or Decimal.")
        elif self._data['amount'] < 0:
            raise ValueError("Payment amount cannot be a negative number.")
        elif self._data['amount'] > 1000:
            raise ValueError("Payment amount cannot be over 10,000.")
        else:
            self.amount = self._data['amount']
            
        if not isinstance(self._data['currency'], str):
            raise TypeError("Payment currency must be of type str.")
        if self._data['currency'] not in PaymentRequest.valid_currencies:
            raise ValueError("Payment currency must be a valid currency code. Refer to 'PaymentRequest.valid_currencies'.")
        else:
            self.currency = self._data['currency']
             
        if not isinstance(self._data['payment_method'], str):
            raise TypeError("Payment currency must be of type str.")
        if self._data['payment_method'] not in PaymentRequest.valid_payment_methods:
            raise ValueError("Payment method must be a valid method string. Refer to 'PaymentRequest.valid_payment_methods'.")
        else:
            self.payment_method = self._data['payment_method']
        
    def __repr__(self):
        return "PaymentRequest(amount: %s, currency: %s, payment_method: %s)" % (self.amount, self.currency, self.payment_method)

    def to_dict(self) -> dict:
        return {
            'amount': self.amount,
            'currency': self.currency,
            'payment_method': self.payment_method,
        }
        

