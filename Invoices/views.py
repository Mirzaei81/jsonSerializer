from rest_framework.response import Response
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

class MainView(RetrieveAPIView):
	queryset = Data.objects.all()
	serializer_class = data_serilaizer
	def get(self, request, *args, **kwargs):
		instance = self.get_object()
		serializer = self.get_serializer(instance)	
		response = {}
		response["success"] = "true"
		response["data"] =serializer.data
		return Response(response)
		



