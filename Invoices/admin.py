from typing import Any
from django.contrib import admin
from django.http import HttpRequest
from django.urls import path
from .views import  Parser
from .models import *
# Register your models here.
class DataInline(admin.StackedInline):
    model = Data
    def get_extra(self, request: HttpRequest, obj: Any | None = ..., **kwargs: Any) -> int:
         return 0
class LicenseInline(admin.StackedInline) :
    model = License
    def get_extra(self, request: HttpRequest, obj: Any | None = ..., **kwargs: Any) -> int:
         return 0

class Inquiry_listInline(admin.TabularInline) :
     model =Inquiry_list
@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    inlines = [
         DataInline,
         LicenseInline
    ]
    list_display = ["uid","code","phone","gender","father_name"]
    search_fields = ["uid"]
    
@admin.register(Inquiry_list)
class Inquiry_listAdmin(admin.ModelAdmin):
	list_display = ["title","result","data_id"]

@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
<<<<<<< HEAD
	list_display = ["Status","PostalCode","Issuer","Address","Issue_date","get_license"] 
	def get_license(self,obj):
            return obj.License.code
=======
    inlines = [
         Inquiry_listInline
    ]
    # list_display = ["Status","PostalCode","Address","Issue_date","Inquiries_lists"] 
>>>>>>> 068d8c4 (fix bug in Admin panel Update File Upload Count Size)
@admin.register(License)
class LicenseAdmin(admin.ModelAdmin):
	list_display =  ["id","code","organization_1",]

class CustomAdminSite(admin.AdminSite):
    def get_urls(self):
        self._registry = admin.site._registry
        admin_urls = super().get_urls() 
        custom_urls = [
            path('parser/', Parser.as_view(admin=self), name="parser"),
        ]
        return custom_urls + admin_urls # custom urls must be at the beginning

    def get(self):
        self.request.current_app == self.name
        return super().get(self.request)

    def get_app_list(self, request,app_label=None):
        app_list = super().get_app_list(request)
        app_list += [
            {
                "name": "Json File Uploader",
                "app_label": "Parser",
                # "app_url": "/admin/test_view",
                "models": [
                    {
                        "name": "Parser",
                        "object_name": "Parser",
                        "admin_url": "/admin/parser/",
                        "view_only": True,
                    }
                ],
            }
        ]
        return app_list

site = CustomAdminSite()