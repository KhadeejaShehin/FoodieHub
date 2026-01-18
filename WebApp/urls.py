from django.urls import path
from WebApp import views

urlpatterns=[
    path('HelloIndex/',views.HelloIndex,name="HelloIndex"),
    path('AboutPage/',views.AboutPage,name="AboutPage"),
    path('ProductsPage/',views.ProductsPage,name="ProductsPage"),
    path('ServicePage/',views.ServicePage,name="ServicePage"),
    path('ContactPage/',views.ContactPage,name="ContactPage"),
    path('SaveContact/',views.SaveContact,name="SaveContact"),
    path('FilterPage/<cat_name>',views.FilterPage,name="FilterPage"),
    path('Single_Item/<int:item_id>/',views.Single_Item,name="Single_Item"),
    path('',views.SignInPage,name="SignInPage"),
    path('SignUpPage/',views.SignUpPage,name="SignUpPage"),
    path('Save_Registration/',views.Save_Registration,name="Save_Registration"),
    path('User_Login/',views.User_Login,name="User_Login"),
    path('User_Logout/',views.User_Logout,name="User_Logout"),
    path('Save_Cart/',views.Save_Cart,name="Save_Cart"),
    path('CartPage/',views.CartPage,name="CartPage"),
    path('DeleteCart/<int:cart_id>/',views.DeleteCart,name="DeleteCart"),
    path('CheckOutPage/',views.CheckOutPage,name="CheckOutPage"),
    path('Save_CheckOut/',views.Save_CheckOut,name="Save_CheckOut"),
    path('PaymentPage/',views.PaymentPage,name="PaymentPage")

]