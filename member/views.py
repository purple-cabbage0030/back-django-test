import json
from django.shortcuts import render
from django.urls import reverse
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Users
from .serializers import UserSerializer

# 회원가입
@api_view(['POST'])
def registrationView(request):
    if request.method == 'POST':
        print('111111111111')
        serializer = UserSerializer(data=request.data)
        print(serializer)
        data = {}
        if serializer.is_valid():
            print('got valid')
            new_user = Users(
                uuid = serializer.validated_data['UUID'], 
                upw = serializer.validated_data['UPW'],
                uage = int(serializer.validated_data['UAGE']), 
                usex = serializer.validated_data['USEX'],
                uheight = float(serializer.validated_data['UHEIGHT']),
                uweight = float(serializer.validated_data['UWEIGHT']),
                uact = serializer.validated_data['UACT'], 
                urdc = float(serializer.validated_data['URDC'])
                )
            new_user.save()
            data['response'] = "회원가입 성공"
            data['uuid'] = new_user.uuid
        else:
            data = serializer.errors
        print(data)
        return JsonResponse(data)

