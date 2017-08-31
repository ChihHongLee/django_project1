from django.contrib import admin
from .models import Record,Category

#model建立完要到admin註冊
# Register your models here.
admin.site.register(Record)
admin.site.register(Category)
