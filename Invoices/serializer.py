from rest_framework import serializers
from .models import Inquiry_list,Data,CustomUser,License
class inquiry_list_serializer(serializers.ModelSerializer):
	class Meta:
		model = Inquiry_list
		fields = '__all__'
class user_serializer(serializers.ModelSerializer):
	gender =serializers.SerializerMethodField()
	def get_gender(self,obj):
		if obj.gender:
			return "1"
		else:
			return "0"

	class Meta:
		model = CustomUser
		fields = ["uid","code","phone","gender","username","father_name"]
	
class licence_serializer(serializers.ModelSerializer):
	class Meta:
		model = License
		fields ="__all__"
class data_serilaizer(serializers.ModelSerializer):
	Issuer =  user_serializer()
	License =  licence_serializer()
	class Meta:
		model = Data
		fields = ["postalCode","Issuer","License","address","issue_date","province","status"] 