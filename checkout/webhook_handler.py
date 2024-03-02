from django.http import HttpResponse

class StripeWH_Handler:
    """ Handle Stripe wen handles """

    def__init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unkown/unexpected/webhook event
        """
        return HttpResponse(
            contents=f'Webhook recieved {event["type"]}',
            status=200)
