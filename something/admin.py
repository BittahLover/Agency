from django.contrib import admin
from .models import Order, Manager, Advertising, Worker, Topic, Customer

admin.site.register(Order)
admin.site.register(Manager)
admin.site.register(Topic)
admin.site.register(Worker)
admin.site.register(Advertising)
admin.site.register(Customer)