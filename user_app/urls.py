from .models import *
from django.urls.conf import path
from django.views.generic.base import RedirectView
from . import views

app_name = 'user'

urlpatterns = [
    path('', RedirectView.as_view(url='dashboard'), name='home'),
    # path('dashboard/', Dashboard.as_view(), name='dashbaord'),
    # path('notifications/<int:id>', NotificationsList.as_view(), name='notifications'),
    # path('user/<int:id>', ViewProfile.as_view(), name='myprofile'),
    # path('cart/', CartList.as_view(), name='cart'),
    # path('card/<int:id>')

    # # Authentication Urls
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    # path('logout/', Logout.as_view(), name='logout'),

    # # Admin Panel Urls
    # path('adminPanel/', AdminPanel.as_view(), name='adminPanel'),
]