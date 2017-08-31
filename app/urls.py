
from django.conf.urls import url
from . import views
# 從當下路徑import views進來

urlpatterns = [
    url(r'^$' , views.frontpage),
    url(r'^settings$' , views.settings),
    url(r'^add_category$',views.addCategory),
    url(r'^add_record$' , views.addRecord),
    url(r'^delete_record$', views.deleteRecord),
    url(r'^delete_category$', views.deleteCategory)
]
