from django.shortcuts import render,redirect
from AdminApp.models import CategoryDB,ProductDB
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from WebApp.models import ContactDb
from django.contrib import messages
# Create your views here.

def AdminIndex(request):
    categories = CategoryDB.objects.count()
    products = ProductDB.objects.count()
    return render(request,"index.html",{'categories': categories,'products':products})

def AddCat(request):
    return render(request,"AddCategory.html")

def SaveCat(request):
    if request.method == 'POST':
        aa = request.POST.get('cat_name')
        bb = request.POST.get('cat_desc')
        img = request.FILES['profile']
        obj = CategoryDB( CategoryName=aa, Description=bb,Category_Image=img)
        obj.save()
        messages.success(request, "Category saved successfully")
        return redirect(AddCat)


def DisplayCat(request):
    register = CategoryDB.objects.all()
    return render(request,"DisplayCategory.html",{'register': register})


def EditCat(request,emp_id):
    data = CategoryDB.objects.get(id=emp_id)
    return render(request,"EditCategory.html",{'data':data})

def UpdateCat(request,data_id):
    if request.method == 'POST':
        aa = request.POST.get('cat_name')
        bb = request.POST.get('cat_desc')
        try:
            img = request.FILES['profile']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = CategoryDB.objects.get(id=data_id).Category_Image
        CategoryDB.objects.filter(id=data_id).update(CategoryName=aa,Description=bb,Category_Image=img)
        messages.success(request, "Category updated successfully")
        return redirect(DisplayCat)


def DeleteCat(request,emp_id):
    Category= CategoryDB.objects.filter(id=emp_id)
    Category.delete()
    messages.error(request, "Category deleted successfully")
    return redirect(DisplayCat)


# *******************************************************************************************
def AddPro(request):
    cat = CategoryDB.objects.all()
    return render(request,"AddProduct.html",{'categories' : cat})


def SavePro(request):
    if request.method == 'POST':

        aa = request.POST.get('pro_select')
        bb = request.POST.get('pro_name')
        cc = request.POST.get('pro_desc')
        dd = request.POST.get('pro_price')
        img = request.FILES['profile']
        obj = ProductDB(Category_Name=aa,ProductName=bb,Description=cc,Price=dd,Product_Image=img)
        obj.save()
        messages.success(request, "Product saved successfully")
        return redirect(AddPro)

def DisplayPro(request):
    register = ProductDB.objects.all()
    return render(request, "DisplayProduct.html", {'register': register})



def EditPro(request,pro_id):
    cat = CategoryDB.objects.all()
    pro = ProductDB.objects.get(id=pro_id)
    return render(request,"EditProduct.html",{'pro' : pro, 'cat' : cat})

def UpdatePro(request,pro_id):
    if request.method == "POST":
        aa = request.POST.get('pro_select')
        bb = request.POST.get('pro_name')
        cc = request.POST.get('pro_desc')
        dd = request.POST.get('pro_price')
        try:
            img = request.FILES['profile']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = ProductDB.objects.get(id=pro_id).Product_Image
        ProductDB.objects.filter(id=pro_id).update(Category_Name=aa, ProductName=bb, Description=cc,Price=dd,Product_Image=img)
        messages.success(request, "Product updated successfully")
        return redirect(DisplayPro)



def DeletePro(request,emp_id):
    Product= ProductDB.objects.filter(id=emp_id)
    Product.delete()
    messages.error(request, "Product deleted successfully")
    return redirect(DisplayPro)


# ****************************************************************************

def AdminLogin(request):
    return render(request,"Admin_Login.html")

def AdminLoginPage(request):
    if request.method == "POST":
        un = request.POST.get('username')
        pswd = request.POST.get('pass')
        if User.objects.filter(username__contains=un).exists():
            x = authenticate(username=un,password=pswd)

            if x is not None:
                request.session['username'] = un
                request.session['password'] = pswd
                login(request,x)
                return redirect(AdminIndex)
            else:
                return redirect(AdminLogin)
        else:
            return redirect(AdminLogin)



def AdminLogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(AdminLogin)




# *********************************************************************
def ContactDetail(request):
    data = ContactDb.objects.all()
    return render(request,"ContactDetails.html",{'data':data})

def DeleteContact(request,con_id):
    Contact= ContactDb.objects.filter(id=con_id)
    Contact.delete()
    return redirect(ContactDetail)



