from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, redirect
from .models import Order
from .forms import OrderForm
import logging


def list_orders(request):
    orders = Order.objects.all()
    return render(request, "orders.html", {'orders': orders})


def create_order(request):
    logger = logging.getLogger('django')
    form = OrderForm(request.POST or None)
    if form.is_valid():
        form.save()
        logger.info(f"order successfully created")
        return redirect('list_orders')
    return render(request, 'form.html', {"form": form})


def update_order(request, id):
    logger = logging.getLogger('django')
    order = Order.objects.get(id=id)
    form = OrderForm(request.POST or None, instance=order)

    if form.is_valid():
        form.save()
        logger.info(f"order has been updated")
        return redirect('list_orders')
    return render(request, 'form.html', {'form': form, 'order': order})


def delete_order(request, id):
    logger = logging.getLogger('django')
    order = Order.objects.get(id=id)

    if request.method == 'POST':
        order.delete()
        logger.info(f"order with id = {id} has been deleted")
        return redirect('list_orders')
    return render(request, 'delete_accept.html', {'order': order})


def main_page(request):
    count = User.objects.count()
    return render(request, 'main_page.html', {
        'count': count
    })


def signup(request):
    logger = logging.getLogger('django')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info(f"person successfully authorized to site")
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })


@login_required
def new_page(request):
    return render(request, 'new_page.html')


class NewPage(LoginRequiredMixin, TemplateView):
    template_name = 'new_page.html'
