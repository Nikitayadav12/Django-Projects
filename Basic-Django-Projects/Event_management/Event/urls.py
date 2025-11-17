from rest_framework.routers import DefaultRouter

from .views import  Eventviewset


router=DefaultRouter()

router.register(r"event",Eventviewset,basename='event')

urlpatterns=router.urls