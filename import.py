from core.wsgi import *
import os
import openpyxl
from backend.models import Region, Wearhouse

book = openpyxl.load_workbook("fff/all.xlsx", read_only=True)
sheet = book.active
row_count = len([row for row in sheet if not all([cell.value is None for cell in row])])
for i in range(3, row_count + 1):
    if str(sheet[f'B{i}'].value) != 'Qoraqalpogiston Respublikasi':
    reg = Region.objects.get(name_uz__contains=str(sheet[f'B{i}'].value))
    print(reg.name_uz)
    print(i)
    Wearhouse.objects.create(name_uz=str(sheet[f'F{i}'].value), name_en=str(sheet[f'F{i}'].value),
                             name_ru=str(sheet[f'M{i}'].value), name_kr=str(sheet[f'I{i}'].value),
                             place=str(sheet[f'C{i}']), region=reg,
                             description_uz=str(sheet[f'E{i}'].value),
                             description_ru=str(sheet[f'L{i}'].value),
                             description_en=str(sheet[f'J{i}'].value),
                             description_kr=str(sheet[f'H{i}'].value),
                             address=str(sheet[f'G{i}'].value),
                             number=str(sheet[f'D{i}'].value)).save()

