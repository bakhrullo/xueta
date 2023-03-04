import os
import openpyxl
from backend.models import Region, LoaderEquipment

for filename in os.listdir("fff"):
    reg = Region.objects.get(name_uz=filename)
    for file in os.listdir(str("fff/"+filename)):
        book = openpyxl.load_workbook("fff/"+filename+"/"+file, read_only=True)
        sheet = book.active
        row_count = len([row for row in sheet if not all([cell.value is None for cell in row])])
        for i in range(3, row_count + 1):
            print(filename + str(sheet[f'C{i}'].value))
            LoaderEquipment.objects.create(name_uz=str(sheet[f'C{i}'].value), name_en=str(sheet[f'C{i}'].value),
                                           name_ru=str(sheet[f'C{i}'].value), type='kran',
                                           region=reg).save()
