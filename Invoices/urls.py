from django.urls import path
from rest_framework import routers
from .views import * 
router = routers.SimpleRouter()
router.register(r"user",UserViewSet,"user")
router.register(r"data-Detail",DataViewSet)
router.register(r"lisance",LicenceViewSet,"lisance")
router.register(r"inquery",InqueryViewSet,"inquery")
<<<<<<< HEAD
urlpatterns = [path("<pk>",MainView.as_view())]+router.urls
=======

urlpatterns = [path("<pk>",MainView.as_view()),path("parser/",Parser.as_view())]+router.urls
>>>>>>> 1e6b517 (Refacotor Changes to match the given JSON File)
