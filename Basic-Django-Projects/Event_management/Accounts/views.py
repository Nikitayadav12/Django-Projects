from django.shortcuts import render

# Create your views here.
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import APIView, api_view

from rest_framework.response import Response
from rest_framework import status

from .serializers import UserSerializer, UserLoginSerializer
from  django.contrib.auth import authenticate



@api_view(['POST'])
def register(request):
    if request.method=='POST':
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            return Response({'msg':'user created successfully'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    if request.method=='POST':
        serializer=UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user=authenticate(username=serializer.validated_data['username'],password=serializer.validated_data['password'])
            if user:
                refresh=RefreshToken.for_user(user)
                return Response({'refresh':str(refresh),'access':str(refresh.access_token)},status=status.HTTP_200_OK)
            return Response({'msg':'Invalid Credential Error'},status=status.HTTP_400_BAD_REQUEST)

        return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)

def home(request):
    return render(request, 'accounts/home.html')

def attendee(request):
    return render(request, 'attendees/register_event.html')

