import os
import json
from datetime import date, datetime, timedelta
import numpy as np
import werkzeug
from PIL import Image

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import serializers, status

from config import settings

from .apps import ApiConfig
from .models import Food, Diet, Train
from .serializers import FoodSerializer, DietSerializer, TrainSerializer

# 음식 분류
@api_view(['GET', 'POST'])
def predictFoodView(request):
    targetx = 128
    targety = 128

    imagefile = request.FILES['image']   # 업로드된 파일 조회
    print(imagefile, type(imagefile))

    image = Image.open(imagefile)   # PIL로 이미지 로딩
    image_cvt = image.convert("RGB")
    image_resize = image_cvt.resize((targetx,targety))    # 모델 input shape
    image_arr = np.array(image_resize)   # PIL 이미지 타입을 ndarray로 변환

    X = np.array(image_arr)
    X = X.astype("float") / 256
    X = X.reshape(-1, targetx, targety,3)

    model = ApiConfig.model
    pred = model.predict(X)  
    categories = [f'F{i}' for i in range(1,20)]
    result = [np.argmax(value) for value in pred]   # 예측 값 중 가장 높은 클래스 반환
    print('New image prediction : ',categories[result[0]])

    fid = categories[result[0]]

    result = Food.objects.get(pk=fid)   # Food 모델 객체
    print(result)
    serializer = FoodSerializer(result)
    print(serializer.data)
    return JsonResponse(serializer.data)

# 식단 기록 저장
@api_view(['POST'])
def dietSaveView(request):
    serializer = DietSerializer(data=request.data)
    print("데이터 받았습니다",request.data)
    data = []
    if serializer.is_valid():
        print('got valid')
        save_data = Diet(
            uuid=serializer.validated_data['uuid'], 
            fid = serializer.validated_data['fid'],
            fname=serializer.validated_data['fname'], 
            meal = serializer.validated_data['meal'], 
            amount=serializer.validated_data['amount'],
            cal=serializer.validated_data['cal'],
            carboh=serializer.validated_data['carboh'],
            protein=serializer.validated_data['protein'],
            fat=serializer.validated_data['fat'])
        save_data.save()
        data['response'] = '저장 성공'
    else:
        data = serializer.errors
    print(data)
    return JsonResponse(data)

# 운동 기록 저장
@api_view(['GET', 'POST'])
def trainSaveView(request):
    serializer = TrainSerializer(data=request.data)
    print("데이터 받았습니다",request.data)
    data = {}
    if serializer.is_valid():
        print('got valid')
        save_data = Train(
            uuid=serializer.validated_data['uuid'], 
            eid = serializer.validated_data['eid'],
            error_name=serializer.validated_data['error_name'], 
            count = serializer.validated_data['count'], 
            error_count=serializer.validated_data['error_count'])
        save_data.save()
        data['response'] = '저장 성공'
    else:
        data = serializer.errors
    print(data)
    return JsonResponse(data)

# 식단 기록 기간별 조회
@api_view(['POST'])
def dietSelectView(request):
    requested_data = request.data
    uuid = requested_data['uuid']
    period = requested_data['period']
    print(uuid, period, type(uuid), type(period))

    end_date = datetime.today()
    start_date = end_date - timedelta(days=period)
    start_date = start_date.replace(microsecond=0, second=0, minute=0, hour=0)
    print(start_date, end_date)

    diet_list = Diet.objects.filter(uuid=uuid, diet_datetime__range=[start_date, end_date])
    data = {'diet_id':[], 'uuid':[], 'diet_datetime':[], 'meal':[], 'fid':[], 'fname':[], 'amount':[], 'cal':[], 'carboh':[], 'protein':[], 'fat':[]}
    for diet in diet_list:
        data['diet_id'].append(diet.pk)
        data['uuid'].append(diet.uuid.uuid)
        data['diet_datetime'].append(diet.diet_datetime.strftime('%m월 %d일'))
        data['meal'].append(diet.meal)
        data['fid'].append(diet.fid.fid)
        data['fname'].append(diet.fname)
        data['amount'].append(diet.amount)
        data['cal'].append(diet.cal)
        data['carboh'].append(diet.carboh)
        data['protein'].append(diet.protein)
        data['fat'].append(diet.fat)
    print(data)
    return JsonResponse(data)

# 운동 기록 기간별 조회
@api_view(['POST'])
def trainSelectView(request):
    requested_data = request.data
    uuid = requested_data['uuid']
    period = requested_data['period']
    print(uuid, period, type(uuid), type(period))

    end_date = date.today()
    start_date = end_date - timedelta(days=period)
    print(start_date, end_date)

    train_list = Train.objects.filter(uuid=uuid, train_date__range=[start_date, end_date])
    data = {'train_id':[], 'uuid':[], 'train_date':[], 'eid':[], 'error_name':[], 'count':[], 'error_count':[]}
    for train in train_list:
        data['train_id'].append(train.pk)
        data['uuid'].append(train.uuid.uuid)
        data['train_date'].append(train.train_date.strftime('%m월 %d일'))
        data['eid'].append(train.eid.eid)
        data['error_name'].append(train.error_name)
        data['count'].append(train.count)
        data['error_count'].append(train.error_count)
    print(data)
    return JsonResponse(data)