from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Users
from .serializers import UserSerializer

# 회원가입
@api_view(['POST'])
def registrationView(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            print('got valid')
            new_user = Users(
                uuid = serializer.validated_data['uuid'], 
                upw = serializer.validated_data['upw'],
                uage = int(serializer.validated_data['uage']), 
                usex = serializer.validated_data['usex'],
                uheight = float(serializer.validated_data['uheight']),
                uweight = float(serializer.validated_data['uweight']),
                uact = serializer.validated_data['uact'], 
                urdc = float(serializer.validated_data['urdc'])
                )
            new_user.save()
            data['response'] = "회원가입 성공"
            data['uuid'] = new_user.uuid
        else:
            data = serializer.errors
        print(data)
        return JsonResponse(data)

    else:
        return Response('method error')

# 회원정보 조회 및 수정
@api_view(['GET', 'POST'])
def userView(request):
    if request.method == 'GET':
        uuid = request.GET['uuid']
        print(uuid)

        user_info = Users.objects.get(pk=uuid)
        serializer = UserSerializer(user_info)
        print(serializer.data)
        return JsonResponse(serializer.data)

    elif request.method == 'POST':
        update_info = request.data
        uuid = update_info['uuid']
        print(uuid)

        update_user = Users.objects.get(pk=uuid)
        update_user.uage = update_info['uage']
        update_user.uheight = update_info['uheight']
        update_user.uweight = update_info['uweight']
        update_user.uact.uact = update_info['uact']
        update_user.urdc = update_info['urdc']
        print(update_user.uage, update_user.uheight)
        update_user.save()
        return Response('저장 성공')

    else:
        return Response('method error')

