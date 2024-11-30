from django.db import models
from django.utils.crypto import get_random_string
from django.core import validators
from django.utils import timezone

provinceChoises = (
	('آذربایجان شرقی','آذربایجان شرقی'),
	( 'آذربایجان غربی','آذربایجان غربی'),
	( 'اردبیل','اردبیل'),
	( 'اصفهان','اصفهان'),
	( 'البرز','البرز'),
	( 'ایلام','ایلام'),
	( 'بوشهر','بوشهر'),
	( 'تهران','تهران'),
	( 'چهارمحال و بختیاری','چهارمحال و بختیاری'),
	( 'خراسان جنوبی','خراسان جنوبی'),
	( 'خراسان رضوی','خراسان رضوی'),
	( 'خراسان شمالی','خراسان شمالی'),
	( 'خوزستان','خوزستان'),
	( 'زنجان','زنجان'),
	( 'سمنان','سمنان'),
	( 'سیستان و بلوچستان','سیستان و بلوچستان'),
	( 'فارس','فارس'),
	( 'قزوین','قزوین'),
	( 'قم','قم'),
	( 'کردستان','کردستان'),
	( 'کرمان','کرمان'),
	( 'کرمانشاه','کرمانشاه'),
	( 'کهگیلویه و بویراحمد','کهگیلویه و بویراحمد'),
	( 'گلستان','گلستان'),
	( 'گیلان','گیلان'),
	( 'لرستان','لرستان'),
	( 'مازندران','مازندران'),
	( 'مرکزی','مرکزی'),
	( 'هرمزگان','هرمزگان'),
	( 'همدان','همدان'),
	( 'یزد','یزد'),
	)
statusChoises = (("صادر شده","صادر شده"),("رد شده","رد شده"))
def randomUID():
	return get_random_string(32,"abcdefghijklmnopqrtuvwxyz123456789")
# Create your models here.
class User(models.Model):
	class phoneValidator(validators.RegexValidator):
		regex = "(?=^[0-9]{11})(?=^09)$"
		message = "Phonenumber is invalid"
	uid = models.CharField("uid",default=randomUID,max_length=32)
	code = models.CharField("code",max_length=255,null=True)
	phone = models.CharField("phone",validators=[phoneValidator],max_length=11,null=True)
	gender = models.BooleanField("gender",default=False,null=True)
	father_name = models.CharField("father_name",max_length=255,null=True)

class License(models.Model):
	_id = models.CharField("_id",default=randomUID,max_length=33)
	code = models.CharField("code",max_length=255)
	organization_1 = models.CharField("organization_1",max_length=255)

class Data(models.Model):
	_id =models.CharField("_id",max_length=33)
	Issuer = models.ForeignKey(User,on_delete=models.CASCADE,related_name="orders")
	License = models.ForeignKey(License,verbose_name="licesne",on_delete=models.CASCADE,related_name="Licences")
	PostalCode = models.CharField("postal_code",max_length=20)
	Address=models.TextField("address",null=True)  
	Province=models.CharField("province",max_length=255,choices=provinceChoises,null=True)
	Status= models.CharField("status",max_length=255,choices=statusChoises,null=True)
	Township=models.CharField("township",max_length=255,null=True)
	Issue_date= models.DateTimeField("issueDate",default=timezone.now)

class Inquiry_list(models.Model):
	resultChoises = (("تایید شده","تایید شده"),("تایید نشده","تایید نشده"))
	title=models.CharField("title",max_length=255,null=True)
	result = models.CharField("result",max_length=255,choices=resultChoises,null=True)
	data = models.ForeignKey(Data,on_delete=models.CASCADE,null=True,related_name="Inquiries_lists")
class TempData(models.Model):
	data = models.TextField()
