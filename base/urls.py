from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view, name='home_view'),
    path('list/', views.ticket_list_view, name='tickets_list_view'),
    path('detail/<str:pk>/', views.ticket_detail, name='detail'),
    path('delete/<str:pk>/', views.ticket_delete, name='delete')

]