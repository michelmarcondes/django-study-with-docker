from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Project, Tag


def paginateProjects(request, projects, results):
    #paginator configuration
    page = request.GET.get('page') #set what result page must load
    paginator = Paginator(projects, results)

    try:
        projects = paginator.page(page) #set results to show according desired page
    except PageNotAnInteger:
        page = 1
        projects = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        projects = paginator.page(page)

    #create a rolling pagination
    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return projects, custom_range




def searchProjects(request):
    search_query = request.GET.get('search_query')

    if not search_query:
        search_query = '' 

    tags = Tag.objects.filter(name__icontains=search_query)

    projects = Project.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(owner__name__icontains=search_query) |
        Q(tags__in=tags)
    )

    return projects, search_query


def getPaginationLink(request, query_set):
    search_query = request.GET.get('search_query')

    pagination_link = ''

    if search_query:
        pagination_link = '?search_query=' + search_query

    if search_query and query_set.has_other_pages():
        pagination_link += '&page='
    elif query_set.has_other_pages():
        pagination_link = '?page='
    else:
        pagination_link = ''

    return pagination_link