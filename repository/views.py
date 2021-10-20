import os
import json
import numpy as np
import werkzeug
from PIL import Image

from django.shortcuts import render
from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from config import settings

from .apps import ApiConfig
from .models import Food, Diet
from .serializers import FoodSerializer, DietSerializer


@api_view(['GET'])
def helloAPI(request):
    return Response('hello world')

@api_view(['GET', 'POST'])
def predictFoodView(request):
    targetx = 128
    targety = 128

    imagefile = request.FILES['image']   # 업로드된 파일 조회
    # filename = werkzeug.utils.secure_filename(imagefile.filename)
    print(imagefile, type(imagefile))
    # print(imagefile.image.width, imagefile.image.height, imagefile.image.format, imagefile.name)

    image = Image.open(imagefile)   # PIL로 이미지 로딩
    image_cvt = image.convert("RGB")
    image_resize = image_cvt.resize((targetx,targety))    # 모델 input shape
    image_arr = np.array(image_resize)   # PIL 이미지 타입을 ndarray로 변환

    # data = np.asarray(image_arr)
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

@api_view(['POST'])
def dietSaveView(request):
    serializer = DietSerializer(data=request.data)
    print("데이터 받았습니다",request.data)
    data = {}
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
        # data['uuid'] - save_data.uuid
    else:
        data = serializer.errors
    print(data)
    return JsonResponse(data)

# @csrf_exempt
# def predict(request):
#     form = forms.UploadForm(request.POST, request.FILES)   # form 객체 생성
#     if form.is_valid():   # is_valid(): 요청파라미터 검증 (True: 검증 성공 / False: 실패)
#         clean_data = form.cleaned_data   # cleaned_data: form으로 넘어온 검증 통과한 요청파라미터 값들 묶어서 딕셔너리로 반환
#         img_field  = clean_data['upimg']   # 업로드된 파일 조회
#         print(img_field, type(img_field))   # 파일명, <class 'django.core.files.uploadedfile.InMemoryUploadedFile'> -- ImageField의 속성들 가져올 수 있음
#         print(img_field.image.width, img_field.image.height, img_field.image.format, img_field.name) #ImageField.name: 파일명
        
#         image = Image.open(img_field)   # PIL로 이미지 로딩
#         image_resize = image.resize((150,150))   # 모델 input shape - (150,150,3)
#         image_arr = np.array(image_resize)   # PIL 이미지 타입을 ndarray로 변환
#         image_arr = image_arr/255.   # 정규화
#         input_tensor = image_arr[np.newaxis, ...]   # 배치축 추가 - (150,150,3) => (1,150,150,3)

#         model = ApiConfig.model
#         pred = model.predict(input_tensor)   # 출력층의 activation함수 sigmoid 사용 - 0.5 기준으로 0이 cat, 1이 dog
#         cls = np.where(pred[0,0]<0.5, 'cat', 'dog') 

#         # 메모리에 임시로 저장되어있는 파일 로컬에 저장
#         save_path = os.path.join(settings.MEDIA_ROOT, img_field.name)
#         print(save_path)
#         image.save(save_path)   # PIL Image객체.save(경로): 이미지 저장
        
        
#         # dictionary -> JSON 변환시 numpy 타입은 변환이 안된다. str(), float()으로 타입변환
#         result = {
#                 'result':str(cls),   # 클래스
#                 'pred':float(pred[0,0]),   # 확률
#                 'img_url':r"/media/{}".format(img_field.name)   # 이미지 저장 경로
#                 }
        
#         result_str = json.dumps(result)   # dictionary를 json문자열로 반환
    
#         return HttpResponse(result_str)
