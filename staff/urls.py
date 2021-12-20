from django.urls import path
from . import views


urlpatterns = [
    
    # path('', views.home, name='home'),
    
    path('', views.staffs, name='staffs'),
    path('staff/<str:pk>/', views.staff, name="staff"),
    # path('emp/<str:pk>/', views.emp, name='emp'),
    
    path('login/', views.loginstaff, name='log'),
    path('logout/', views.logoutstaff, name='logout'),
    
    path('account/', views.account, name='acc'),
    path('edit-acc/', views.editacc, name='edit-acc'),
    
   
    
    
]
