from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(Product)
admin.site.register(Categories)
admin.site.register(Medium,Medium_display)