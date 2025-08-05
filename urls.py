"""
URL configuration for hostel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from hostell import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('adminlogin',views.adminlogin,name="adminlogin"),

    path('usersignup',views.usersignup,name='usersignup'),
    path('userlogin',views.userlogin,name="userlogin"),
    path('logout/',views.LogoutPage,name='logout'),
    path('admindash/',views.admindash,name="admindash"),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('mark_attendance/', views.mark_attendance, name='mark_attendance'),
    path('attendance/', views.attendance, name='attendance'),
    path('roomalloc/',views.roomalloc,name="roomalloc"),
    path('admin_room_allocation/', views.admin_room_allocation, name='admin_room_allocation'),
    path('visitor_entry/', views.visitor_entry, name='visitor_entry'),
    path('visitor_success/', views.visitor_success, name='visitor_success'),
    path('mainnavbar',views.mainnavbar,name="mainnavbar"),
    path('navbar',views.navbar,name="navbar"),
    path('index',views.index,name="index"),
    path('userdash',views.userdash,name='userdash'),
    path('roombook/',views.roombook,name='roombook'),
    path('usercomplaints/', views.user_complaints, name='usercomplaints'),
    path('admin_complaints_dashboard/', views.admin_complaint_dashboard, name='admin_complaints'),
    path('complaint_success/', lambda request: render(request, 'complaint_success.html'), name='complaint_success'),
    path('mess/',views.mess,name='mess'),
    path('outpass/',views.outpass,name='outpass'),
    path('student_notices/', views.student_notices, name='student_notices'),
    path('payment/', views.payment_page, name='process_payment'),
    path('payment_success/', views.payment_success, name='payment_success'),
    path('profile/',views.profile,name='profile')
]
