from .models import StudentData,groupdata
from .serializer import StudentSerializer,groupserializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['GET'])
def details(request):
    group=groupdata.objects.all()
    # student = StudentData.objects.all()
    grpserializer = groupserializer(group, many=True)
    # stuserializer = StudentSerializer(student, many=True)

    return Response(grpserializer.data)




# @api_view(['POST'])
# def create(request):
#     grpserializer = groupserializer(data=request.data)
#     if grpserializer.is_valid():
#         group = grpserializer.save()
#     request.data['group'] = group.id
#     stuserializer = StudentSerializer(data=request.data)
#     if stuserializer.is_valid():
#          stuserializer.save()
#     return Response(stuserializer.data)



@api_view(['POST'])
def create(request):
    grpserializer = groupserializer(data=request.data)
    if grpserializer.is_valid():
        grpserializer.save()
    return Response(grpserializer.data)


@api_view(['POST'])
def update(request, id):
    student = groupdata.objects.get(id=id)
    grpserializer = groupserializer(instance=student, data=request.data)
    if grpserializer.is_valid():
        grpserializer.save()
    return Response(grpserializer.data)


@api_view(['DELETE'])
def delete1(request, id):
    event = groupdata.objects.get(id=id)
    event.delete()
    return Response('Deleted')



