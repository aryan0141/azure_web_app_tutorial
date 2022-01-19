from django.shortcuts import render
from .models import CustomUser, Resume
from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import CustomUserSerializer, ResumeSerializer, UserRegistrationSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner

# Create your views here.
class UserRegistrationAPIView(APIView):
    serializer_class = UserRegistrationSerializer
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)

            response_data =  {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': serializer.data,
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLogoutAPIView(APIView):
    def post(self, request, format=None):
        try:
            token = request.data.get("refresh_token")
            token_obj = RefreshToken(token)
            token_obj.blacklist()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class UserProfileAPIView(APIView):
    permission_classes = [IsAuthenticated, IsOwner]
    user_serializer_class = CustomUserSerializer
    resume_serializer_class = ResumeSerializer
    def get(self, request, format=None):
        user = request.user
        if user.isDeleted == True:
            return Response({"Error": "No User Found"}, status=status.HTTP_400_BAD_REQUEST)
        serialized_users = CustomUserSerializer(user).data
        return Response(serialized_users, status=status.HTTP_200_OK)

    def delete(self, request, format=None):
        user = request.user
        
        # Soft Deletion of User
        user.isDeleted = True
        user.is_active = False
        user.save()
        return Response({"Success" : "User successfully deleted"}, status=status.HTTP_200_OK)

    def put(self, request, format=None):
        user = request.user
        data = request.data
        print(data)
        user_serializer = self.user_serializer_class(user, data=data)
        resume_serializer = self.resume_serializer_class(data=data, context={'request' : request})
        if user_serializer.is_valid():
            user_serializer.save()
            if ('resume_name' in data) or ('resume_path' in data):
                if resume_serializer.is_valid():
                    # Updating the Old Resume
                    oldresume = Resume.objects.filter(user=user, is_latest=True).first()
                    if oldresume:
                        oldresume.is_latest = False
                        oldresume.save()
                    # Adding new resume
                    resume_serializer.save()
                    return Response({"Success": "User & Resume successfully updated"}, status=status.HTTP_200_OK)
                else:
                    return Response(resume_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({"Success": "User successfully updated"}, status=status.HTTP_200_OK)
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
