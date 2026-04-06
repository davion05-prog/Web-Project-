from django.urls import path
from . import views

app_name = 'assignments'

urlpatterns = [
    path('', views.assignment_list, name='list'),
    path('calendar/', views.calendar_view, name='calendar'),
    path('<int:pk>/', views.assignment_detail, name='detail'),
]



