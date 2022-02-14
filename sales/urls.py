from django.urls import path

from .views import (
    home_view,
    HomeListView,
    SaleDetailView
)

app_name = 'home'

urlpatterns = [
    path('', home_view, name='home'),
    path('sales/', HomeListView.as_view(), name='list'),
    path('sales/<pk>/', SaleDetailView.as_view(), name='detail'),
]
