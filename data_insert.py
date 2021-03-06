import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'
os.environ['DJANGO_ALLOW_ASYNC_UNSAFE'] = 'true'

import django
django.setup()

import pandas as pd
from member.models import Activity
from repository.models import Exercise, Food

def act_data_insert():
    act_data = pd.read_json('master_data/activity.json', encoding='utf-8')
    val = act_data.to_dict('list')
    print(val, len(act_data))

    for i in range(len(act_data)):
        act = Activity(uact=val['uact'][i], val=round(val['val'][i], 1))
        act.save()

def food_data_insert():
    food_data = pd.read_csv('master_data/foodtable1.csv', encoding='cp949')
    menus = food_data.to_dict('list')
    print(menus, len(food_data))

    for i in range(len(food_data)):
        new_menu = Food(fid=menus['FID'][i],fname=menus['FNAME'][i],famount=menus['FAMOUNT'][i],\
                    fcal=menus['FCAL'][i],fcarboh=menus['FCARBOH'][i],fprotein=menus['FPROTEIN'][i],\
                    ffat=menus['FFAT'][i])
        new_menu.save()

def exe_data_insert():
    exercise_data = pd.read_json('master_data/exercise.json', encoding='utf-8')
    val = exercise_data.to_dict('list')
    print(val, len(exercise_data))

    for i in range(len(exercise_data)):
        exe = Exercise(eid=val['eid'][i], ename=val['ename'][i])
        exe.save()

if __name__ == '__main__':
    act_data_insert()
    food_data_insert()
    exe_data_insert()