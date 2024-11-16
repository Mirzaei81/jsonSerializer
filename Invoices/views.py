from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ModelViewSet
from .models import Data,CustomUser,License,Inquiry_list
from .serializer import data_serilaizer,user_serializer,inquiry_list_serializer,licence_serializer

# Create your views here.

class DataViewSet(ModelViewSet):
	queryset = Data.objects.all()
	serializer_class = data_serilaizer
class InqueryViewSet(ModelViewSet):
	queryset = Inquiry_list.objects.all()
	serializer_class =inquiry_list_serializer
class UserViewSet(ModelViewSet):
	queryset = CustomUser.objects.all()
	serializer_class = user_serializer
class LicenceViewSet(ModelViewSet):
	queryset =License.objects.all()
	serializer_class =licence_serializer
	renderer_classes = [JSONRenderer]
