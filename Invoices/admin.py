from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
	list_display = ["uid","code","phone","gender","username","father_name"]
@admin.register(Inquiry_list)
class Inquiry_listAdmin(admin.ModelAdmin):
	list_display = ["title","result","data__id"]
@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
	list_display = ["Status","PostalCode","Issuer","License__organization_1","Address","Issue_date",
				 ] #"province"
@admin.register(License)
class LicenseAdmin(admin.ModelAdmin):
	list_display =  ["_id","code","organization_1",]
