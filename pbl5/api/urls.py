from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_chart, name='show_chart'),
    path('data/', views.get_chart, name='get_chart'),
    path('hr/', views.get_data, name='get_data'),
    path('hr/<int:id>', views.get_data_detail, name='get_data_detail'),
]