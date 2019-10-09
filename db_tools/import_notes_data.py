# 独立使用django的model
import sys
import os
#  获取当前文件的路径，以及路径的父级文件夹名
pwd = os.path.dirname(os.path.realpath(__file__))
# 将项目目录加入setting
sys.path.append(pwd + "../")
# manage.py中
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mangostreetSerDjango.settings")

import django
django.setup()

# 这行代码必须在初始化django之后
from notes.models import Note

# from db_tools.data.note_data import row_data

row_data = [

]

for lev1_cat in row_data:
    lev1_intance = Note()
    lev1_intance.code = lev1_cat["code"]
    lev1_intance.name = lev1_cat["name"]
    lev1_intance.category_type = 1
    lev1_intance.save()