from django.db import models
from django.contrib.auth.models import AbstractUser
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
class CustomUser(AbstractUser):
	class phoneValidator(validators.RegexValidator):
		regex = "(?=^[0-9]{11})(?=^09)$"
		message = "Phonenumber is invalid"
	uid = models.CharField("uid",unique=True,default=randomUID,max_length=32)
	code = models.IntegerField("code",null=True)
	phone = models.CharField("phone",unique=True,validators=[phoneValidator],max_length=11)
	gender = models.BooleanField("gender",default=False)
	father_name = models.CharField("father_name",max_length=255)
class License(models.Model):
	_id = models.CharField("_id",unique=True,default=randomUID,max_length=33)
	code = models.CharField("code",max_length=255)
	organization_1 = models.CharField("organization_1",max_length=255)
class Data(models.Model):
	Issuer = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="orders")
	License = models.ForeignKey(License,verbose_name="licesne_id",on_delete=models.CASCADE,related_name="Licences")
	PostalCode = models.CharField("postal_code",max_length=20)
	Address=models.TextField("address")  
	Province=models.CharField("province",max_length=255,choices=provinceChoises)
	Status= models.CharField("status",max_length=255,choices=statusChoises)
	Township=models.CharField("township",max_length=255),
	Issue_date= models.DateField("issueDate",default=timezone.now)

class Inquiry_list(models.Model):
	resultChoises = (("تایید شده","تایید شده"),("رد شده","رد شده"))
	title=models.CharField("title",max_length=255)
	result = models.CharField("result",max_length=255,choices=resultChoises)
	data = models.ForeignKey(Data,on_delete=models.CASCADE,related_name="Inquiries_lists")

