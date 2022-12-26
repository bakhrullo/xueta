from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(ProductCategory)
admin.site.register(Category)
admin.site.register(User)
admin.site.register(Customs)
admin.site.register(Region)
admin.site.register(Wearhouse)
admin.site.register(InternationalLogisticCompany)
admin.site.register(LocalLogisticCompany)
admin.site.register(LoaderService)
admin.site.register(LoaderEquipment)