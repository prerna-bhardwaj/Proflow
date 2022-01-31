from django.urls.conf import path
from .models import *
from . import views

app_name = 'proj_app'

urlpatterns = [
    # path('viewCommunities', views.viewCommunities, name='viewCommunities'),
    path('', views.home, name='home'),
]
