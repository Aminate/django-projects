from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterUserSerializer, UserSerializer
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model


User = get_user_model()

class RegisterUserAPIView(APIView):
    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=201)
    
# listing - всех user

@api_view(['GET'])
def users_list_api_view(request):
    queryset = User.objects.all()
    serializer = UserSerializer(queryset, many=True)
    return Response(serializer.data)


class Users(User):
    def user(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)