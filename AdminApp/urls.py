from django.urls import path
from AdminApp import views

urlpatterns=[
    path('AdminIndex/',views.AdminIndex,name="AdminIndex"),
    path('AddCat/',views.AddCat,name="AddCat"),
    path('SaveCat/',views.SaveCat,name="SaveCat"),
    path('DisplayCat/',views.DisplayCat,name="DisplayCat"),
    path('EditCat/<int:emp_id>/',views.EditCat,name="EditCat"),
    path('UpdateCat/<int:data_id>/',views.UpdateCat,name="UpdateCat"),
    path('DeleteCat/<int:emp_id>/',views.DeleteCat,name="DeleteCat"),
    # ************************************************************************
    path('AddPro/',views.AddPro,name="AddPro"),
    path('SavePro/',views.SavePro,name="SavePro"),
    path('DisplayPro/',views.DisplayPro,name="DisplayPro"),
    path('EditPro/<int:pro_id>/',views.EditPro,name="EditPro"),
    path('UpdatePro/<int:pro_id>/',views.UpdatePro,name="UpdatePro"),
    path('DeletePro/<int:emp_id>/',views.DeletePro,name="DeletePro"),
    # *************************************************************************
    path('AdminLogin/',views.AdminLogin,name="AdminLogin"),
    path('AdminLoginPage/',views.AdminLoginPage,name="AdminLoginPage"),
    path('AdminLogout/',views.AdminLogout,name="AdminLogout"),
    # ****************************************************************************
    path('ContactDetail/',views.ContactDetail,name="ContactDetail"),
    path('DeleteContact/<int:con_id>/',views.DeleteContact,name="DeleteContact")

]
