from django.shortcuts import render
from django.urls import reverse
import werkzeug
from django.http import JsonResponse


from models import Food, Diet
from classification_model import food_model

def foodselect(request):
    if(request.method == 'POST'):
        fid = ''
        imagefile = ''
        result = ''
        food = []
        filename =''
        ans = ''
        imagefile = request.files['image']
        filename = werkzeug.utils.secure_filename(imagefile.filename)
        imagefile.save('./classification_model/photos/' + filename)
        fid = food_model.image_data(filename)
        print('아이디입니다',fid,'==='*50)

        result = Food.objects.get(pk=fid)   # Food 모델 객체

        # fid 제외 나머지 데이터 str ??
        



        food = list(map(str,result[2:]))
        food.insert(0,result[1])
        ans = ','.join(food)
        print('전송데이터',ans)

        return JsonResponse({'data':ans})
