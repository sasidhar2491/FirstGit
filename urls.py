from .views import *
from django.urls import path

urlpatterns = [
    path('details/', details),
    path('create/', create),
    path('update/<int:id>/', update),
    path('delete/<int:id>/', delete1),
    ]