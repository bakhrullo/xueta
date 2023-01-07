from typing import List, Any
from asgiref.sync import sync_to_async
from backend.models import *
import pandas as pd
from math import isnan


def add_data(): 
    dfUz = pd.read_excel('avtokranToshUz.xlsx')
    dfEn = pd.read_excel('avtokranToshEn.xlsx')
    dfRu = pd.read_excel('avtokranToshRu.xlsx')
    for i in dfUz.index:
        if dfRu["Телефон номер"][i]:
            region = Region.objects.get(name_uz="Toshken viloyati")
            loader_service = LoaderService.objects.create(
                phone = dfRu["Телефон номер"][i],
                tonnas = dfRu["Тоннa"][i],
                region = region,
                type_uz = "Avtokran",
                type_en = dfEn["Autocrane"][i],
                type_ru = dfRu["Автокран"][i],
            )
            loader_service.save()

@sync_to_async
def add_user(user_id, referal_user=None):
    try:
        user, created = User.objects.get_or_create(user_id=user_id)
        user.save()
        return user
    except Exception as exx:
        print(exx)
        return None

    
@sync_to_async
def get_user(user_id):
    try:
        user = User.objects.filter(user_id=user_id).first()
        return user    
    except:
        return None


@sync_to_async
def get_lang(user_id):
    try:
        user = User.objects.filter(user_id=user_id).first()
        return user.lang
    except Exception as exx:
        print(exx)
        return None


@sync_to_async
def get_loader_equipments(type, region):
    print(LoaderEquipment.objects.all()[0].type)
    try:
        region = Region.objects.get(id=region)
        equipments = LoaderEquipment.objects.filter(region=region, type=type).all()
        return equipments
    except Exception as exx:
        print(exx)
        return None


@sync_to_async
def get_all_customs():
    try:
        customs = Customs.objects.all()
        return customs
    except Exception as exx:
        print(exx)
        return None


@sync_to_async
def get_regions():
    try:
        regions = Region.objects.all()
        return regions
    except Exception as exx:
        print(exx)
        return None


@sync_to_async
def get_region(region_id):
    try:
        region = Region.objects.filter(id=region_id).first()
        return region
    except Exception as exx:
        print(exx)
        return None


@sync_to_async
def get_wearhouse(id):
    try:
        wearhouse = Wearhouse.objects.filter(id=id).first()
        return wearhouse
    except Exception as exx:
        print(exx)
        return None

@sync_to_async
def get_post(id):
    try:
        post = PostService.objects.filter(id=id).first()
        return post
    except Exception as exx:
        print(exx)
        return None


@sync_to_async
def get_wearhouse_by_region(region_id):
    try:
        wearhouses = Wearhouse.objects.filter(region__id=region_id).all()
        return wearhouses
    except Exception as exx:
        print(exx)
        return None


@sync_to_async
def get_region_wearhouses(region_id):
    try:
        wearhouses = Wearhouse.objects.filter(region__id=region_id).all()
        return len(wearhouses)
    except Exception as exx:
        print(exx)
        return None


@sync_to_async
def get_region_posts(region_id):
    try:
        wearhouses = PostService.objects.filter(region__id=region_id).all()
        return len(wearhouses)
    except Exception as exx:
        print(exx)
        return None


@sync_to_async
def get_one_customs(id):
    try:
        customs = Customs.objects.get(id=id)
        return customs
    except Exception as exx:
        print(exx)
        return None


@sync_to_async
def get_equipments(type):
    try:
        equipments = LoaderEquipment.objects.filter(type=type)
        return equipments
    except Exception as exx:
        print(exx)
        return None


@sync_to_async
def get_loaders(region):
    try:
        loaders = LoaderService.objects.filter(region__id=region).all()
        return loaders
    except Exception as exx:
        print(exx)
        return None


@sync_to_async 
def get_product_category_by_name(name):
    try:
        categories = ProductCategory.objects.all()
        category = []
        for i in categories:
            if i.name_en == name or i.name_ru == name or i.name_uz == name:
                category = i
        return category
    except Exception as exx:
        print(exx)
        return None


@sync_to_async 
def get_category_by_name(name):
    try:
        categories = Category.objects.all()
        category = []
        for i in categories:
            if i.name_en == name or i.name_ru == name or i.name_uz == name:
                category = i
        return category
    except Exception as exx:
        print(exx)
        return None


@sync_to_async
def get_adresses():
    data = []
    adresses = Wearhouse.objects.all()
    for i in adresses:
        d = {
            "lon": float(i.longitude),
            "lat": float(i.latitude),
            "id": i.id,
        }
        data.append(d)
    return data