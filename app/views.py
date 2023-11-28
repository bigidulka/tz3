from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Item
import stripe
from django.http import HttpResponse
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

def home_view(request):
    return HttpResponse("<h1>Welcome to My Django Project</h1>")

def get_item(request, item_id):
    item = Item.objects.get(id=item_id)
    return render(request, 'item.html', {'item': item})

def buy_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if item.currency == 'EUR':
        stripe.api_key = settings.STRIPE_SECRET_KEY_EUR
    else:
        stripe.api_key = settings.STRIPE_SECRET_KEY

    try:
        intent = stripe.PaymentIntent.create(
            amount=item.price,
            currency=item.currency,
            payment_method_types=['card'],
        )
        return JsonResponse({'clientSecret': intent.client_secret})
    except stripe.error.StripeError as e:
        # Обработка ошибок Stripe
        return JsonResponse({'error': str(e)}, status=403)