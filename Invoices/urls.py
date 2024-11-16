from django.urls import path
from rest_framework import routers
from .views import * 
router = routers.SimpleRouter()
router.register(r"user",UserViewSet,"user")
router.register(r"data-Detail",DataViewSet)
router.register(r"lisance",LicenceViewSet,"lisance")
router.register(r"inquery",InqueryViewSet,"inquery")
urlpatterns = router.urls