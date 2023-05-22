from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',dashboard,name='dashboard'),
    path('login/',login,name='login'),
    path('myprofile/',myprofile,name='myprofile'),
    path('logout/',logout,name='logout'),
    path('secretorylogin/',secretorylogin,name='secretorylogin'),
    path('secretory_dashboard/',secretory_dashboard,name='secretory_dashboard'),
    path('secretory_profile/',secretory_profile,name='secretory_profile'),
    path('secretory_logout/',secretory_logout,name='secretory_logout'),
    path('society_members/',society_members,name='society_members'),
    path('watchman_login/',watchman_login,name='watchman_login'),
    path('watchman_logout/',watchman_logout,name='watchman_logout'),
    path('watchman_profile/',watchman_profile,name='watchman_profile'),
    path('watchman_dashboard/',watchman_dashboard,name='watchman_dashboard'),
    path('society_members2/',society_members2,name='society_members2'),
    path('visitors/',visitors,name='visitors'),
    path('visitors3/',visitors3,name='visitors3'),
    path('visitors2/',visitors2,name='visitors2'),
    path('register/',register,name='register'),
    path('secretory_register/',secretory_register,name='secretory_register'),
    path('watchman_register/',watchman_register,name='watchman_register'),
    path('eventadd/',eventadd,name='eventadd'),
    path('membersevent/',membersevent,name='membersevent'),
    path('watchmanevent/',watchmanevent,name='watchmanevents'),
    path('noticeadd/',noticeadd,name='noticeadd'),
    path('notice_members/',notice_members,name='notice_members'),
    path('notice_watchman/',notice_watchman,name='notice_watchman'),
    path('society_watchman/',society_watchman,name='society_watchman')


]    