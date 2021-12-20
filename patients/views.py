from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import customform, patientform, medform, testform
from .models import Patient, Meds, Tests

from django.db import connection
# Create your views here.

# def patients(request):
    
#     return render(request, 'main.html')

def loginuser(request):
    page='login'
    if request.user.is_authenticated:
        return redirect('account')
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
            return redirect(request.GET['next'] if 'next' in request.GET else 'account')
        else:
            messages.error(request, 'Username or password incorrect') 
            
    context = {'page': page}           
                 
    return render(request, 'login_reg.html', context)


def logoutuser(request):
    logout(request)
    messages.info(request, 'Logged out successfully!') 
    return redirect('home')


def registeruser(request):
    page  = 'register'
    form = customform()
    if request.method == "POST":
        print("")
        form = customform(request.POST)
        # print(form)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            print("saved")
            messages.success(request, 'User created successfully!')
            print(connection.queries)
            
            login(request, user)
            return redirect('edit-account')
        
        else:
            messages.error(request, 'An error occurred while registering. Please try again!')
            
    context = {'page': page, 'form': form}         
    return render(request, 'login_reg.html', context)



@login_required(login_url='login')
def account(request):
    
    patient = Patient.objects.get(user=request.user)
    medss = patient.meds_set.all()
    testss = patient.tests_set.all()
    context = {'patient': patient, 'medss': medss, 'testss':testss}
    
    return render(request, 'account.html', context)



@login_required(login_url='login')
def editaccount(request):
    print('1')
    patient = Patient.objects.get(user=request.user)
    print('2')
    form = patientform(instance=patient)
    print()
    
    if request.method == 'POST':
        print('3')
        form  = patientform(request.POST, request.FILES, instance=patient)
        print('4')
        if form.is_valid():
            form.save()
            print('form:', form)
            print(connection.queries)
            return redirect('account')
        else:
            print('')
    
    context = {'form': form} 
    return render(request, 'edit_form.html', context)


@login_required(login_url='login')
def createmed(request):
    # powner = request.user.username
    patient = Patient.objects.get(user=request.user)
    form = medform()
    
    
    if request.method == 'POST':
        form = medform(request.POST)
        if form.is_valid():
            meds = form.save(commit=False)
            meds.mowner = patient
            meds.mcost = Meds.objects.values_list('mcost', flat=True).get(mname=request.POST.get('mname'))
            # meds.mcost = Meds.objects.get(mcost)
            meds.save()
            messages.success(request, 'Medicine added successfully!')
            return redirect('account')


    context = {'form': form}
    return render(request, 'med_form.html', context)

@login_required(login_url='login')
def createtest(request):
    patient = Patient.objects.get(user=request.user)
    form = testform()
    
    if request.method == 'POST':
        form = testform(request.POST)
        if form.is_valid():
            tests = form.save(commit=False)
            tests.towner = patient
            tests.tcost = Tests.objects.values_list('tcost', flat=True).get(tname=request.POST.get('tname'))
            # tests.tcost = Tests.objects.get(tcost=tcost)
            tests.save()
            messages.success(request, 'Test booked successfully!')
            return redirect('account')


    context = {'form': form}
    return render(request, 'test_form.html', context)

    









