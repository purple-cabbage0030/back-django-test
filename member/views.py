import json
from django.shortcuts import render
from django.urls import reverse
from django.http import JsonResponse

from .models import Users

# 회원가입
def signup(request):
    if(request.method == 'POST'):
        user_data = json.loads(request.body)
        print(user_data, type(user_data))

        new_user = Users(uuid = user_data['UUID'], upw = user_data['UPW'],\
                         uage = int(user_data['UAGE']), usex = user_data['USEX'], \
                         uheight = float(user_data['UHEIGHT']), uweight = float(user_data['UWEIGHT']),\
                         uact = user_data['UACT'], urdc = float(user_data['URDC']))

    print(new_user.uuid)
    new_user.save()

    if new_user.uuid:
        return JsonResponse(result= "id :" +request.form.get("id") 
        +"회원가입 완료. 로그인 페이지로 이동합니다.")
    else:
        return ""
