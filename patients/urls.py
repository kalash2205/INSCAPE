from django.urls import path
from . import views


urlpatterns = [
    
    
    path('login/', views.loginuser, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('register/', views.registeruser, name='register'),
    
    path('account/', views.account, name='account'),
    path('edit-account/', views.editaccount, name='edit-account'),
    
    path('create-med/', views.createmed, name='create-med'),
    path('create-test/', views.createtest, name='create-test'),
    
]
    
