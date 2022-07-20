from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.parsers import MultiPartParser, FormParser
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
import json
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .serializers import (UserSerializerWithToken, UserResgisterSerializer, UserOutSerializer, 
        ProfileCreateSerializer)

from authentication.models import Profile

class LoginUser(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

register_response = openapi.Response("response")
@swagger_auto_schema(methods=["POST"], request_body=UserResgisterSerializer,
        responses={200: UserSerializerWithToken(many=False)})
@api_view(['POST'])
def registerUser(request):
    data = request.data
    try:
        user = User.objects.create(
            username = data["username"],
            password = make_password(data["password"])
        )
        print(user)
        serializer = UserSerializerWithToken(user, many=False)
        return Response({"response":"success", "data": serializer.data}, status=status.HTTP_201_CREATED)
    except:
        return Response({"response":"error"})

class ProfileCreateView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    @swagger_auto_schema(request_body=ProfileCreateSerializer)
    def post(self, request):
        try:
            user = request.user
            data = request.data
            data._mutable = True
            data["user"] = user.id
            data._mutable = False
            serializer = ProfileCreateSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"response":"error"}, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(request_body=ProfileCreateSerializer)
    def put(self, request):
        try:
            user = request.user
            data = request.data
            data._mutable = True
            data['user'] = user.id
            data._mutable = False
            profile = Profile.objects.get(user=user)
            serializer = ProfileCreateSerializer(profile, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({"response":"success", "data": serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"response": "error"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"response":"error"}, status=status.HTTP_404_NOT_FOUND)

class ProfileDelete(APIView):
    permission_classes = [IsAdminUser]
    def delete(self, request, pk):
        try:
            profile = Profile.objects.get(pk=pk)
            profile.delete()
            return Response({"response": "success"}, status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({"response": "error"}, status=status.HTTP_403_FORBIDDEN)