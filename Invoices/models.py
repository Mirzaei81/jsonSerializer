from django.db import models
from django.utils import timezone
# Create your models here.
class User(models.Model):
	uid = models.CharField("uid",max_length=32,null=True)
	code = models.CharField("code",max_length=255,null=True)
	phone = models.CharField("phone",max_length=11,null=True)
	gender = models.BooleanField("gender",default=False,null=True)
	father_name = models.CharField("father_name",max_length=255,null=True)

class License(models.Model):
	_id = models.CharField("_id",max_length=33,null=True)
	code = models.CharField("code",max_length=255,null=True)
	organization_1 = models.CharField("organization_1",max_length=255,null=True)
	Issuer= models.ForeignKey(User,verbose_name="issuer",null=True,on_delete=models.CASCADE,related_name="Licences")

class Data(models.Model):
	_id =models.CharField("_id",max_length=33,null=True)
	PostalCode = models.CharField("postal_code",max_length=20,null=True)
	Address=models.TextField("address",null=True)  
	Province=models.CharField("province",max_length=255,null=True)
	Status= models.CharField("status",max_length=255,null=True)
	Township=models.CharField("township",max_length=255,null=True)
	Issue_date= models.DateTimeField("issueDate",default=timezone.now)
	Issuer= models.ForeignKey(User,on_delete=models.CASCADE,related_name="Datas",null=True)

class Inquiry_list(models.Model):
	resultChoises = (("تایید شده","تایید شده"),("تایید نشده","تایید نشده"))
	title=models.CharField("title",max_length=255,null=True)
	result = models.CharField("result",max_length=255,choices=resultChoises,null=True)
	data = models.ForeignKey(Data,on_delete=models.CASCADE,null=True,related_name="Inquiries_lists")
class TempData(models.Model):
	data = models.TextField()
