from .models import  Department, Staff, Specialities

from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def searchstaffs(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        
    specialitiess = Specialities.objects.filter(sname__icontains=search_query)        
        
    staffs = Staff.objects.distinct().filter(
        Q(name__icontains=search_query)|
        # Q(department__in=search_query) | 
        Q(specialities__in=specialitiess)
        # Q(qualification__icontains=search_query)     
    )   
    # profiles = Profile.objects.distinct().filter(Q(name__icontains=search_query) | Q(intro__icontains=search_query) | Q(skill__in=skills))
         
    return staffs, search_query


def paginate(request, staffs, results):
    page = request.GET.get('page')
    paginator = Paginator(staffs, results)

    try:
        staffs = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        staffs = paginator.page(page)
    except EmptyPage:
        page=paginator.num_pages 
        staffs = paginator.page(page)   
    
    leftindex = (int(page)-1)
    rightindex = (int(page)+2)

    if leftindex <1:
        leftindex=1
    if rightindex> paginator.num_pages:
        rightindex=paginator.num_pages +1

    custom_range = range(leftindex, rightindex)
    return custom_range, staffs 
         
