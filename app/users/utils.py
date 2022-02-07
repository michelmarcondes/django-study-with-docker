from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Profile, Skill


def paginateProfiles(request, profiles, results):
    #paginator configuration
    page = request.GET.get('page') #set what result page must load
    paginator = Paginator(profiles, results)

    try:
        profiles = paginator.page(page) #set results to show according desired page
    except PageNotAnInteger:
        page = 1
        profiles = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        profiles = paginator.page(page)

    #create a rolling pagination
    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return profiles, custom_range

def searchProfiles(request):
    search_query = request.GET.get('search_query')

    if not search_query:
        search_query = ''    

    skills = Skill.objects.filter(name__icontains=search_query)

    # filter as case insensitive and using OR operator with Q support
    profiles = Profile.objects.distinct().filter(
          Q(name__icontains=search_query) | 
          Q(short_intro__icontains=search_query) |
          Q(skill__in=skills)
    )

    return profiles, search_query