from django.contrib import admin
from django.urls import path, include
from something import views

urlpatterns = [
    path('', views.main_page, name='home'),
    path('list_orders/', views.list_orders, name='list_orders'),
    path('create_order/', views.create_order, name='create_order'),
    path('update_order/<int:id>/', views.update_order, name='update_order'),
    path('delete_order/<int:id>/', views.delete_order, name='delete_order'),
    path('signup/', views.signup, name='signup'),
    path('new/', views.new_page, name='new'),
    path('newPage/', views.NewPage.as_view(), name='newPage'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
