from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(number)
admin.site.register(otp_verify)
admin.site.register(final_otp) 
admin.site.register(qr_code)