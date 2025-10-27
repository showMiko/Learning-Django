from django.urls import path
from . import views
urlpatterns = [
    path('', views.all_basic_view, name='all_basic'),
]
