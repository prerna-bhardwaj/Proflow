from .models import Notifications
from django.urls.conf import path
from . import views
from django.views.generic.base import RedirectView


app_name = 'login'

urlpatterns = [
    path('', RedirectView.as_view(url='dashboard'), name='home'),
    # path('dashboard/', Dashboard.as_view(), name='dashbaord'),
    # path('notifications/', NotificationsList.as_view(), name='notifications'),
    # path('user/<int:id>', ViewProfile.as_view(), name='myprofile'),
    # path('cart/', CartList.as_view(), name='cart'),

    # # Authentication Urls
    # path('signin/', UserLogin.as_view(), name='signin'),
    # path('signup/', UserSignup.as_view(), name='signup'),
    # path('logout/', Logout.as_view(), name='logout'),

    # # Admin Panel Urls
    # path('adminPanel/', AdminPanel.as_view(), name='adminPanel'),
]