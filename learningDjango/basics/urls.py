from django.urls import path
from . import views
urlpatterns = [
    path('', views.all_basic_view, name='all_basic'),
    path('item/<int:item_id>/', views.details_view, name='item_details'),
    path('forms/', views.forms_view, name='forms_view'),
]
