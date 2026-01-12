from django.shortcuts import render
from .models import User
from rest_framework.response import Response
from rest_framework import status
from .serailizer import UserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    # check if user already exists
    user = User.objects.filter(username=request.data.get("username")).exists()

    if user:
        return Response({'message': 'User already exists.'}, status=status.HTTP_400_BAD_REQUEST)
    
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    