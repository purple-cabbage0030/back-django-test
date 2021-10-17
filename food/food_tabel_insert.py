import os
import django
import pandas as pd
from models import Food

os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'   # root/config/settings.py 경로 지정
os.environ['DJANGO_ALLOW_ASYNC_UNSAFE'] = 'true'
django.setup()

data = pd.read_csv('foodtable1.csv',encoding='cp949')
menus = data.to_dict('list')
print(menus,len(data))

for i in range(len(menus)):
    new_menu = Food(fid=menus['FID'][i],fname=menus['FNAME'][i],famount=menus['FAMOUNT'][i],\
                 fcal=menus['FCAL'][i],fcarboh=menus['FCARBOH'][i],fprotein=menus['FPROTEIN'][i],\
                 ffat=menus['FFAT'][i])
    new_menu.save()