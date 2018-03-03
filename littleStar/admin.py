from django.contrib import admin
from littleStar.models import UserProfileInfo, User,CreateSchool,kiddetails,anthropometry,Dental,Pediatrics

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(CreateSchool)
admin.site.register(kiddetails)
admin.site.register(anthropometry)
admin.site.register(Dental)
admin.site.register(Pediatrics)
