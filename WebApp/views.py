from django.shortcuts import render,redirect
from AdminApp.models import CategoryDB,ProductDB
from WebApp.models import ContactDb,RegistrationDb,CartDb,OrderDb
from django.contrib import messages
import razorpay
# Create your views here.

def HelloIndex(request):
    Categories = CategoryDB.objects.all()
    cart_total = CartDb.objects.filter(Username=request.session['UserName'])
    x = cart_total.count()
    return render(request,"Home.html",{'Categories':Categories,'x':x})
def AboutPage(request):
    Categories = CategoryDB.objects.all()
    cart_total = CartDb.objects.filter(Username=request.session['UserName'])
    x = cart_total.count()
    return render(request,"About.html",{'Categories':Categories,'x':x})

def ProductsPage(request):
    Products = ProductDB.objects.all()
    Categories = CategoryDB.objects.all()
    cart_total = CartDb.objects.filter(Username=request.session['UserName'])
    x = cart_total.count()
    return render(request,"Products.html",{'Products':Products,'Categories': Categories,'x':x})

def ServicePage(request):
    Categories = CategoryDB.objects.all()
    cart_total = CartDb.objects.filter(Username=request.session['UserName'])
    x = cart_total.count()
    return render(request,"Service.html",{'Categories':Categories,'x':x})

def ContactPage(request):
    Categories = CategoryDB.objects.all()
    cart_total = CartDb.objects.filter(Username=request.session['UserName'])
    x = cart_total.count()
    return render(request,"Contact.html",{'Categories':Categories,'x':x})

def SaveContact(request):
    if request.method == "POST":
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        sub = request.POST.get('Subject')
        msg = request.POST.get('Message')
        obj = ContactDb( Name=name,Email=email,Subject=sub,Message=msg)
        obj.save()
        messages.success(request, "Submited Sucessfully")
        return redirect(ContactPage)

def FilterPage(request,cat_name):
    Categories = CategoryDB.objects.all()
    data = ProductDB.objects.filter(Category_Name=cat_name)
    cart_total = CartDb.objects.filter(Username=request.session['UserName'])
    x = cart_total.count()
    return render(request,"Filtered_Items.html",{'data': data,'Categories':Categories,'x':x})

def Single_Item(request, item_id):
    product = ProductDB.objects.get(id=item_id)
    Categories = CategoryDB.objects.all()
    cart_total = CartDb.objects.filter(Username=request.session['UserName'])
    x = cart_total.count()
    return render(request,"Single_Item.html",{'product': product,'Categories':Categories,'x':x})



# *******************************************************************************

def SignInPage(request):
    return render(request,"SignIn.html")

def SignUpPage(request):
    return render(request,"SignUp.html")

def Save_Registration(request):
    if request.method == "POST":
         name = request.POST.get('username')
         ps1 = request.POST.get('pass1')
         ps2 = request.POST.get('pass2')
         email = request.POST.get('email')
         obj = RegistrationDb(UserName=name,Password1=ps1,Password2=ps2,Email=email)
         obj.save()
         messages.success(request, "Registered Sucessfully")
         return redirect(SignInPage)

def User_Login(request):
    if request.method == "POST":
        un = request.POST.get('username')
        pswd = request.POST.get('pass')
        if RegistrationDb.objects.filter(UserName=un,Password1=pswd).exists():
            request.session['UserName'] = un
            request.session['Password1'] = pswd
            messages.success(request, "Welcome")
            return redirect(HelloIndex)
        else:
            messages.warning(request, "Failed to login")
            return redirect(SignInPage)
    else:
        messages.warning(request, "Failed to login")
        return redirect(SignInPage)


def User_Logout(request):
    del request.session['UserName']
    del request.session['Password1']
    return redirect(SignInPage)

def Save_Cart(request):
    if request.method=="POST":
        pname=request.POST.get('pname')
        qty = request.POST.get('quantity')
        pr = request.POST.get('price')
        tot = request.POST.get('total')
        uname = request.POST.get('username')
        try:
            x = ProductDB.objects.get(ProductName=pname)
            img = x.Product_Image
        except ProductDB.DoesNotExist:
            img=None
        obj = CartDb(Username=uname,ProductName=pname,Quantity=qty,Price= pr,TotalPrice=tot,Prod_Image=img)
        obj.save()
        return redirect(HelloIndex)



def CartPage(request):
    sub_total = 0
    shipping_amount = 0
    total_amount = 0
    Categories  = CategoryDB.objects.all()
    data = CartDb.objects.filter(Username=request.session['UserName'])
    for i in data:
        sub_total += i.TotalPrice
        if sub_total>500:
            shipping_amount=50
        else:
            shipping_amount=100
        total_amount = sub_total + shipping_amount
        cart_total = CartDb.objects.filter(Username=request.session['UserName'])
        x = cart_total.count()
    return render(request,"Cart.html",{'Categories': Categories , 'data' : data,'sub_total':sub_total,'total_amount':total_amount,'shipping_amount':shipping_amount,'x':x})

def DeleteCart(request,cart_id):
    Cart=CartDb.objects.filter(id=cart_id)
    Cart.delete()
    return redirect(CartPage)

def CheckOutPage(request):
    sub_total = 0
    shipping_amount = 0
    total_amount = 0
    Categories = CategoryDB.objects.all()
    data = CartDb.objects.filter(Username=request.session['UserName'])
    for i in data:
        sub_total += i.TotalPrice
        if sub_total > 500:
            shipping_amount = 50
        else:
            shipping_amount = 100
        total_amount = sub_total + shipping_amount
        cart_total = CartDb.objects.filter(Username=request.session['UserName'])
        x = cart_total.count()
    return render(request, "Checkout.html",
                  {'Categories': Categories, 'data': data, 'sub_total': sub_total, 'total_amount': total_amount,
                   'shipping_amount': shipping_amount,'x':x})


def Save_CheckOut(request):
    if request.method=="POST":
        name=request.POST.get('Name')
        email = request.POST.get('Email')
        place = request.POST.get('Place')
        address = request.POST.get('Address')
        mobile = request.POST.get('Mobile')
        pincode = request.POST.get('Pincode')
        total_price = request.POST.get('Amount')
        message = request.POST.get('Message')
        obj = OrderDb(Name=name, Email=email, Place=place, Address=address, Mobile=mobile, Pincode=pincode,
                      TotalPrice=total_price, Message=message)
        obj.save()
        return redirect(PaymentPage)

def PaymentPage(request):
    Username=request.session['UserName']
    #Retrieve the data from OrderDb with the specified ID
    customer = OrderDb.objects.order_by('-id').first()
    #Get the amount of the specified customer
    payy = customer.TotalPrice
    #convert the amount into paisa (smallest currency unit)
    amount = int(payy*100)    #Assuming the amount in rupess
    payy_str = str(amount)


    if request.method == "POST":
        order_currency = 'INR'
        client = razorpay.Client(auth=('rzp_test_Rp9vnULrNQLrkn','vTEmD1BEvpWJ4k9nn0OBNEGj'))
        payment = client.order.create({'amount':amount,'currency':order_currency})
    return render(request,"Payment.html",{'Username':Username,'customer':customer,'payy_str':payy_str})