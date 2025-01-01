from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer, RegisterSerializer, ProfileSerializer
from rest_framework import generics
from .models import CustomUser
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
# Create your views here.
@api_view(['GET', 'POST'])
def welcome_view(request):
    if request.method == 'GET':
        return Response({'message': 'Welcome to the API!'})
    
#Login user
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

#Register User
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

#api/profile  and api/profile/update
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProfile(request):
    user = request.user
    serializer = ProfileSerializer(user, many=False)
    return Response(serializer.data)

@swagger_auto_schema(method='patch', request_body=ProfileSerializer)
@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def updateProfile(request):
    user = request.user
    serializer = ProfileSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)