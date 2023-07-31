from django.db import models

# Create your models here.
class number(models.Model):
    phone_number = models.IntegerField(blank=False, null=False)
    
class otp_verify(models.Model):
    otp = models.IntegerField(blank=True, null=True)
    
class final_otp(models.Model):
    f_otp = models.IntegerField(blank=False, null=False)
    
class qr_code(models.Model):
    qr_code_value = models.IntegerField(blank=False, null=False)
    
class upload(models.Model):
    upload_file = models.FileField(blank=False, null=False)