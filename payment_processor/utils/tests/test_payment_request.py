from django.test import TestCase

from utils.payment_request import PaymentRequest


class TestPaymentRequest(TestCase):

    def test_request_valid(self):
        request = PaymentRequest(request={
            'amount': 29.99,
            'currency': 'USD',
            'payment_method': 'paypal',
        })

        self.assertEqual(request.amount, 29.99)
        self.assertEqual(request.currency, 'USD')
        self.assertEqual(request.payment_method, 'paypal') 

    def test_amount_invalid_type_raises_type_error(self):
        with self.assertRaises(TypeError):
            request = PaymentRequest(request={
                'amount': '10',
                'currency': 'USD',
                'payment_method': 'card',
             })

    def test_amount_negative_value_raises_value_error(self):
        with self.assertRaises(ValueError):
            request = PaymentRequest(request={
                'amount': -10,
                'currency': 'USD',
                'payment_method': 'card',
             })    

    def test_amount_large_value_raises_value_error(self):
        with self.assertRaises(ValueError):
            request = PaymentRequest(request={
                'amount': 10001,
                'currency': 'USD',
                'payment_method': 'card',
             })
            
    def test_currency_invalid_type_raises_type_error(self):
        with self.assertRaises(TypeError):
            request = PaymentRequest(request={
                'amount': 10,
                'currency': 101,
                'payment_method': 'card',
             })
    
    def test_currency_invalid_value_raises_value_error(self):
        with self.assertRaises(ValueError):
            request = PaymentRequest(request={
                'amount': 10,
                'currency': 'US',
                'payment_method': 'card',
             })
            
    def test_payment_method_invalid_type_raises_type_error(self):
        with self.assertRaises(TypeError):
            request = PaymentRequest(request={
                'amount': 10,
                'currency': 'USD',
                'payment_method': 101,
             })
    
    def test_currency_invalid_value_raises_value_error(self):
        with self.assertRaises(ValueError):
            request = PaymentRequest(request={
                'amount': 10,
                'currency': 'USD',
                'payment_method': 'some_method',
             })