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

