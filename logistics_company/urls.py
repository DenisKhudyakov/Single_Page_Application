from django.urls import path

from logistics_company.apps import LogisticsCompanyConfig
from logistics_company.views import MainTableListView

app_name = LogisticsCompanyConfig.name


urlpatterns = [
    path('', MainTableListView.as_view(), name='main'),
]