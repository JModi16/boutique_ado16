from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from checkout.models import Order, OrderLineItem
from products.models import Product
import stripe
import json


@require_POST
@csrf_exempt
def webhook(request):
    """Listen for webhooks from Stripe"""
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE', '')
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret
        )
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)
    except Exception as e:
        return HttpResponse(content=e, status=400)

    # Handle the event
    if event['type'] == 'payment_intent.succeeded':
        intent = event['data']['object']
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        # Fulfill the purchase, send the customer an email, etc.
        # That's where you'd put your 20 lines of code so this function doesn't timeout
        try:
            order = Order.objects.get(stripe_pid=pid)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        except Order.DoesNotExist:
            order = None
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | ERROR: Order not found',
                status=404)

    elif event['type'] == 'payment_intent.payment_failed':
        intent = event['data']['object']
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    return HttpResponse(content=f'Webhook received: {event["type"]}', status=200)