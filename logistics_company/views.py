from django.core.paginator import Paginator
from django.shortcuts import render

from logistics_company.models import Registry


def order_list(request):
    """Функция для отображения списка заказов"""
    orders = Registry.objects.all()
    paginator = Paginator(orders, 5)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    return render(request, 'logistics_company/main.html', {'page_obj': page_obj})




