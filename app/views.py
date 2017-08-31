from django.shortcuts import render  ,redirect
from .models import Record , Category
from .forms import RecordForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def say_hello(request):   #request使用者發訴的起請求
    a=1
    return render(request, 'app/hello.html' )
# view是在app下面做處理template里的東東
#
@login_required
def frontpage(request):
    record_form = RecordForm(initial={'balance_type':'支出'})
    records = Record.objects.filter()  #ORM語法，把Record物件資料全取出來

    income_lst = [x.cash for x in records if x.balance_type=='收入']
    outcome_lst = [x.cash for x in records if x.balance_type=='支出']
    income=sum(income_lst) if income_lst else 0
    outcome=sum(outcome_lst) if outcome_lst else 0
    net = income - outcome
    #要把records供給以下template使用
    '''
    return render(request ,'app/old_index.html' , {'records':records,'income':income,
                                                    'outcome':outcome,'net':net} )
   '''
    return render(request ,'app/old_index.html' ,locals()) #使用locals載入所有變數

@login_required
def settings(request):
    categories = Category.objects.filter()
    return render(request,'app/settings.html',locals())
@login_required
def addCategory(request):
    if request.method == 'POST':
        posted_data = request.POST
        category = posted_data['add_category']
        Category.objects.get_or_create(category=category)

    #用下面寫法，可以將上面事情做完後 導到指定URL
    return redirect('/settings')

@login_required
def addRecord(request):
    if request.method=='POST':
        form =RecordForm(request.POST) #用modelform塞dic給from
        if form.is_valid():
            form.save()
    return redirect('/')

@login_required
def deleteRecord(request):
    if request.method=='POST':
        id = request.POST['delete_val']
        Record.objects.filter(id=id).delete()
    return redirect('/')

@login_required
def deleteCategory(request):
    if request.method=='POST':
        category = request.POST['delete_category']
        Category.objects.filter(category=category).delete()
    return redirect('/settings')

'''
--------------------------------------------------------------------
logout
'''
from django.contrib import auth

def logout(request):
    auth.logout(request)
    return redirect('/')
