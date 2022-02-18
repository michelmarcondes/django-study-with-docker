from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response 

from .serializers import ProjectSerializer
from projects.models import Project, Review


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET': '/api/projects'},
        {'GET': '/api/projects/id'},
        {'GET': '/api/projects/id/vote'},

        {'POST': '/api/token'},
        {'POST': '/api/token/refresh'},
    ]

    return Response(routes)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getProjects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True) # set object to serialize and define 'many' to retrive more than a single record
    return Response(serializer.data)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getProject(request, pk):
    project = Project.objects.get(id=pk)
    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def projectVote(request, pk):
    project = Project.objects.get(id=pk)
    profile = request.user.profile
    data = request.data

    review, created = Review.objects.get_or_create(
        owner = profile,
        project = project,
    )

    review.value = data['vote']
    review.save()

    print(review)

    # update vote count
    project.getVoteCount


    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)