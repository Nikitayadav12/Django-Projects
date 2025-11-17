from django.urls  import path
from .views import RegisterEventView


urlpatterns=[
    path('register/<int:event_id>/',RegisterEventView.as_view(),name='event_register')
]
from .views import register_event_form,  your_api_view

urlpatterns = [
    path('register/', register_event_form, name='register_event_form'),  # for showing form
    path('register/api_register_event/<int:event_id>/', your_api_view, name='api_register_event'),# for API call

]

