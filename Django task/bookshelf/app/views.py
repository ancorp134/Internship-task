from pickle import TRUE
from .models import BookShelf
from .serializer import BookShelfSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view



@api_view(['GET'])
def BookShelf_Details(request):
    
    if request.method =='GET':
        data=BookShelf.objects.all()
        serializer=BookShelfSerializer(data,many=TRUE)
        return Response(serializer.data)


@api_view(['GET'])
def BookShelf_SingleRecord(request,pk):
    
    if request.method =='GET':
        data=BookShelf.objects.get(id=pk)
        serializer=BookShelfSerializer(data)
        return Response(serializer.data)
    
    
@api_view(['POST'])
def Add_Record(request):

    if request.method =='POST':
        serializer=BookShelfSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    