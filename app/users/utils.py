from django.db.models import Q

from .models import Profile, Skill


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