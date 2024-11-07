"""
    path('', views.home, name=''),
    path('orders/', views.order, name=''),
    path('orders/<orderId>/', views.order, name=''),
    path('cart-items/', views.cart-item, name=''),
    path('checkout/', views.checkout, name=''),
    path('users/', views.user, name=''),
    path('users/<userId>', views.user, name=''),
"""

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
