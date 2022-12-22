import datetime
from typing import List, Any
from asgiref.sync import sync_to_async
from backend.models import *


@sync_to_async
def add_user(user_id, referal_user):
    try:
        user, created = User.objects.get_or_create(user_id=user_id)
        if user.referal_user:
            pass
        else:
            user.referal_user = referal_user
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
def get_all_customs():
    try:
        customs = Customs.objects.all()
        return customs
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


