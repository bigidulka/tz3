from django.urls import path
from .views import get_item, buy_item

urlpatterns = [
    path('item/<int:item_id>/', get_item, name='get_item'),
    path('buy/<int:item_id>/', buy_item, name='buy_item'),
]