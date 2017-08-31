from django.db import models
from django.db.models import CharField, DateField, ForeignKey, IntegerField
#model建立完要到admin註冊

# Create your models here.

BALANCE_TYPE=((u'收入',u'收入'),(u'支出',u'支出'))
            #((key,val) ,())

class Category(models.Model):  #交通 飲食 ...
    category = CharField(max_length=20)
    def __str__(self):#  當此物件被print時，以__str__內容顯示
        return self.category

class Record(models.Model):
    date        = DateField()
    description = CharField(max_length=300)
    category    = ForeignKey(Category , on_delete=models.SET_NULL,null=True)
    cash        = IntegerField()
    balance_type= CharField(max_length=2,choices=BALANCE_TYPE)     #收支
    def __str__(self):
        return  self.description +' ('+ str(self.date) +')'
#model建立完要到admin註冊
    '''
    ForeignKey的 on_delete 參數
    關聯欄位被刪除時，依下面參數做觸發
    --------------------------------
    models.CASCADE   ->交通被刪除，ubike也會被刪除
    models.PROTECT   ->不允許被刪除
    models.SET_NULL :要搭配null=True    ->交通被刪掉，ubike的分類就變null
    models.SET_DEFAULT: 要搭配default   ->交通被刪調，ubkie變default

    '''
