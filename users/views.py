from django.shortcuts import render
from .models import CustomUser, Resume
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import CustonUserSerializer, ResumeSerializer, UserRegistrationSerializer
from rest_framework.parsers import MultiPartParser
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


class UsersAPIView(APIView):
    parser_classes = (MultiPartParser,)
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = ResumeSerializer
    def get(self, request, format=None):
        resumes = Resume.objects.filter(user=request.user)
        serialized_resumes = ResumeSerializer(resumes, many=True).data
        # users = CustomUser.objects.all()
        # serialized_users = CustonUserSerializer(users, many=True).data
        return Response(serialized_resumes, status=status.HTTP_200_OK)

    def delete(self, request, format=None):
        user = request.user
        if user.is_authenticated:
            user.isDelete = True
            user.save()
            return Response({"Success" : "User successfully deleted"}, status=status.HTTP_200_OK)
        else:
            return Response({"Error": "User must be authenticated to delete data"}, status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data, context={'request' : request})
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            # file_uploaded = request.FILES.get('resume_file')
            # content_type = file_uploaded.content_type
            return Response(serialized_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        data = request.data
        print(data["first_name"])
        return Response("Hello World")


class ResumesAPIView(APIView):
    parser_classes = (MultiPartParser,)
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = ResumeSerializer
    def post(self, request, format=None):
        return Response(status=status.HTTP_200_OK)