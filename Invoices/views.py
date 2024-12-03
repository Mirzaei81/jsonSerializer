from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ModelViewSet
import json
from .forms import InputForm
from .models import Data,User,License,Inquiry_list,TempData
from .serializer import data_serilaizer,user_serializer,inquiry_list_serializer,licence_serializer,main_serilaizer
from .utils import CaseInsensitiveDict
from django.views.generic import FormView
from datetime import datetime

# Create your views here.
class DataViewSet(ModelViewSet):
	queryset = Data.objects.all()
	serializer_class = data_serilaizer
class InqueryViewSet(ModelViewSet):
	queryset = Inquiry_list.objects.all()
	serializer_class =inquiry_list_serializer
class UserViewSet(ModelViewSet):
	queryset = User.objects.all()
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
		response["data"] = serializer.data
		return Response(response)
def HandleJsonUpload(data,ctx)->list[User,Data,License]:
	# Loadding a file ot dict via json .load and then converting it to caseInsentive one
	data = CaseInsensitiveDict(data["data"])
	user =User(uid=data["user"]["uid"],
		code=data["user"]["code"] ,
		phone=data["user"]["phone"],
		gender=data["user"]["gender"],
		father_name=data["user"]["father_name"]
		)
	license = License(_id=data["license"]["_id"],
				code=data["license"]["code"],
				Issuer=user,
				organization_1=data["license"]["organization_1"])
	mainData = Data(_id=data["_id"],
		Issuer=user,
		PostalCode=data["postal_code"],
		Address=data["address"],
		Province=data["province"],
		Status=data["status"],
		Township=data["township"],
		Issue_date=datetime.strptime(data["Issue_date"],"%Y-%m-%dT%H:%M:%S.%fZ")
	)
	inquirieslist = []
	for iq in data["inquiry_list"]:
		inquirieslist.append(Inquiry_list(title=iq["title"],result=iq["result"],data=mainData))
	if not "inquiry_list" in ctx:
		ctx["inquiry_list"] = inquirieslist
	else:
		ctx["inquiry_list"] +=inquirieslist
	if not "user" in ctx:
		ctx["user"] = [user]
	else:
		ctx["user"] += [user]
	if not "data" in ctx:
		ctx["data"] =[mainData]
	else:
		ctx["data"] +=[mainData]
	if not "license" in ctx:
		ctx["license"] = [license]
	else:
		ctx["license"]  += [license]
	ctx["userHeader"] = ["uid","code","phone","gender","father_name"]
	ctx["dataHeader"] =["id","PostalCode","Address","Province","Status","Township","Issue_date"]
	ctx["licenseHeader"] = [f for f in license.__dict__ if not f.startswith("_")]
	return [user,mainData,license,inquirieslist]

class Parser(FormView):
	admin = {}
	form_class = InputForm
	def get(self, request):
		ctx = self.admin.each_context(request)
		ctx.update(self.get_context_data())
		return render(request, 'admin/parser.html', ctx)
	def form_valid(self, form) -> HttpResponse:
		files = form.cleaned_data["files_field"]
		if form.is_valid():
			ctx = self.admin.each_context(self.request)
			ctx.update(self.get_context_data())
			total =[]
			for f in files:
				data= json.load(f)
				total.append(data)	
				try:
					HandleJsonUpload(data,ctx)
				except Exception as e : 
					ctx["error"] = e
					return render(self.request, 'admin/parser.html', ctx)
			temp = TempData.objects.create(data=json.dumps(total))
			ctx["temp_id"] = temp.id
			temp.save()
			return  render(self.request,"admin/success.html",ctx)
		return render(self.request, 'admin/parser.html', ctx)
	def put(self, *args, **kwargs):
		id =self.request.GET.get("tempId")
		print(id)
		comitedFile = TempData.objects.get(id=id)
		data= json.loads(comitedFile.data)
		for d in data:
			user,mainData,license,inquirieslist = HandleJsonUpload(d,{})
			user.save()
			mainData.save()
			license.save()
			for iq in inquirieslist:
				iq.save()
		comitedFile.delete()
		return render(self.request,"admin/confirmed.html")


