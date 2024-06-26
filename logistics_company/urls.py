from django.urls import path

from logistics_company.apps import LogisticsCompanyConfig
from logistics_company.views import order_list

app_name = LogisticsCompanyConfig.name


urlpatterns = [
    path('', order_list, name='main'),
]