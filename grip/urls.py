
from django.contrib import admin
from django.urls import path
from creditmanage import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('user',views.users,name='users'),
    path('profile/<int:pk>',views.profile,name='profile'),
    path('transactions',views.viewtransactions,name='viewtransactions'),
    path('passbook/<int:pk>',views.viewpassbook,name='viewpassbook')
]
