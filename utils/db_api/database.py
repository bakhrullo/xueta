from typing import List, Any
from asgiref.sync import sync_to_async
from backend.models import *
import pandas as pd
from math import isnan


def add_data(): 
    dfUz = pd.read_excel('tif2.xlsx')
    dfEn = pd.read_excel('tifEn.xlsx')
    dfRu = pd.read_excel('tifRu.xlsx')
    for i in dfUz.index:
        name_ru = ""
        name_en = ""
        address_ru = ""
        address_en = ""
        region = ""
        regions = Region.objects.all()
        for reg in regions:
            if reg.name_uz in dfUz["Manzil"][i]:
                region = reg
        for j in dfEn.index:
            if not isnan(dfEn["Post code"][j]) and int(dfUz["Post Kodi"][i]) == int(dfEn["Post code"][j]):
                print(dfEn["Post code"][j])
                name_ru = dfRu["Название постов УГТК Республики Узбекистан"][j]
                name_en = dfEn["Name of posts of territorial departments of the state Customs Committee of the Republic of Uzbekistan"][j]
                custom = Customs.objects.create(
                    name_uz=dfUz["Nomi"][i],
                    name_ru=name_ru,
                    name_en=name_en,
                    region=region,
                    longitude=dfUz["lon"][i],
                    latitude=dfUz["lat"][i],
                    contact=dfUz["Telefon"][i]
                )
                custom.save()
        
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
def get_customs_by_region(region):
    try:
        customss = Customs.objects.filter(region__id=region).all()
        return customss
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


@sync_to_async
def get_sertification_max_page():
    try:
        return len(Sertification.objects.all()) // 10 + 1
    except Exception as exx:
        print(exx)
        return None


@sync_to_async
def get_sertification_count():
    try:
        return len(Sertification.objects.all())
    except Exception as exx:
        print(exx)
        return None
    
    
@sync_to_async
def get_sertification(id):
    try:
        sert = Sertification.objects.get(id=id)
        return sert
    except Exception as exx:
        print(exx)
        return None


@sync_to_async
def get_by_tonna(tonna, region):
    try:
        min = int(tonna.split("-")[0])
        max = int(tonna.split("-")[1])
        data = []
        services = LogisticService.objects.filter(region__id=region).all()
        for service in services:
            try:
                if int(service.tonna) >= min and int(service.tonna) <= max:
                    data.append(service)
                else:
                    continue
            except Exception as exx:
                continue
        return data
    except Exception as exx:
        print(exx)
        return None

    
@sync_to_async
def logistic_pagination(page, data):
    try:
        objects = data[(int(page)-1) * 15 : int(page) * 15]
        return objects
    except Exception as exx:
        print(exx)
        return None


@sync_to_async
def get_logistic_service_max_page(data):
    try:
        return len(data) // 15 + 1
    except Exception as exx:
        print(exx)
        return None


@sync_to_async
def get_tenved(kod):
    try:
        tenved = TnVed.objects.get(kod=kod)
        return tenved
    except Exception as exx:
        print(exx)
        return None
    

@sync_to_async
def get_tenved_id(id):
    try:
        tenved = TnVed.objects.get(id=id)
        return tenved
    except Exception as exx:
        print(exx)
        return None
    
