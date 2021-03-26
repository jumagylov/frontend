from django.urls import path
from .views import customers_detail, customers_list


urlpatterns = [
    path('api/customers/list', customers_list),
    path('api/customers/detail/<int:pk>', customers_detail),
]
