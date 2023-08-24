from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serialisers import UserCreateSerializer



class UserCreateView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serialiser = UserCreateSerializer(data=request.data)
        if serialiser.is_valid():
            user = serialiser.save()
            return Response({"massage":'user created saccessfilly'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)