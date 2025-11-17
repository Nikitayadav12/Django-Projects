from django.urls import path
from .views import employee_list  # Correct import

urlpatterns = [
    path('employees/', employee_list),
]
