from django.http import HttpResponse

class StripeWH_Handler:
    """
    Handle Stripe webhooks
    """

    def __innit__(self, request)