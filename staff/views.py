from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Staff

from .utilities import paginate, searchstaffs
from .forms import staff_form

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.

# def staffs(request):
#     return render(request, 'staffs.html')

# def staff(request):
#     return render(request, 'staff.html')

def test(request):
    return render(request, 'test.html')

def test2(request):
    return render(request, 'test2.html')

def home(request):
    return render(request, 'home.html')

def creator(request):
    return render(request, 'creator.html')

def contact(request):
    return render(request, 'contact.html')

def lab(request):
    return render(request, 'lab.html')

def pharma(request):
    return render(request, 'pharma.html')

def spec(request):
    return render(request, 'spec.html')


def loginstaff(request):
    page='log'
    if request.user.is_authenticated:
        return redirect('acc')
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')
            
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'acc')
        else:
            messages.error(request, 'Username or password incorrect')    
            
    context = {'page': page}        
                 
    return render(request, 'staff/login.html', context)
    
    

def logoutstaff(request):
    logout(request)
    messages.info(request, 'Logged out successfully!')
     
    return redirect('home')


def staffs(request):
    staffs, search_query = searchstaffs(request)
    custom_range, staffs = paginate(request, staffs, 3)
    context = {'staffs': staffs, 'search_query': search_query, 'custom_range': custom_range}
    return render(request, 'staff/staffs.html', context)


def staff(request, pk):
    staff = Staff.objects.get(id=pk)
    specialitiess = staff.specialities_set.all()
    context = {'staff': staff, 'specialitiess': specialitiess} 
    return render(request, 'staff/staff.html', context)


@login_required(login_url='log')
def account(request):
    staff = Staff.objects.get(user=request.user)
    # skills= profile.skill_set.all()
    # projects = profile.project_set.all()
    specialitiess = staff.specialities_set.all()
    
    
    context = {'staff': staff, 'specialitiess': specialitiess}
    
    return render(request, 'staff/account.html', context)


@login_required(login_url='log')
def editacc(request):
    staff = Staff.objects.get(user=request.user)
    form = staff_form(instance=staff)
    
    if request.method == 'POST':
        form  = staff_form(request.POST, request.FILES, instance=staff)
        if form.is_valid():
            form.save()
            return redirect('acc')
    
    context = {'form': form}
    
    return render(request, 'staff/edit_form.html', context)


