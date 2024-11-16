from rest_framework	import serializers
from .models import	Inquiry_list,Data,User,License

class inquiry_list_serializer(serializers.ModelSerializer):
	id = serializers.CharField(source="_id")
	class Meta:
		model =	Inquiry_list
		fields = ['id','title','result','data']

class user_serializer(serializers.ModelSerializer):
	gender =serializers.SerializerMethodField()
	def	get_gender(self,obj):
		if obj.gender:
			return 1
		else:
			return 0

	class Meta:
		model =User
		fields = ["uid","code","phone","gender","username","father_name"]
	
class licence_serializer(serializers.ModelSerializer):
	_id = serializers.CharField(source="id")
	class Meta:
		model =	License
		fields =["_id","code","organization_1"]

class data_serilaizer(serializers.ModelSerializer):
	_id = serializers.CharField(source="id")
	Issuer =  user_serializer()
	License	=  licence_serializer()
	Issue_date = serializers.DateTimeField(format="%b-%m-%d %H:%M:%S.%f",input_formats=["%Y-%m-%dT%H:%M:%S.%fZ"])
	def validate_Issuer(self,value):
		return value
	class Meta:
<<<<<<< HEAD
		model = Data
		fields = ["PostalCode","Issuer","License","Address","Issue_date","Province","Status"] 
=======
		model =	Data
		fields = ["PostalCode","Issuer","License","Address","Issue_date","Province","Status"] 
class main_serilaizer(serializers.Serializer):
	_id = serializers.CharField(source="id")
	postal_code= serializers.CharField()
	license_id=	serializers.IntegerField()
	address= serializers.CharField()
	province= serializers.CharField()
	township= serializers.CharField()
	issue_date=	serializers.DateField()
	status=	serializers.CharField()
	inquiry_list=inquiry_list_serializer(many=True)	
	user=user_serializer()
	license= licence_serializer()
>>>>>>> 1e6b517 (Refacotor Changes to match the given JSON File)
