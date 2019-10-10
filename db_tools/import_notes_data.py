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

import pymongo

myclient = pymongo.MongoClient("mongodb://192.168.0.104:27017/")
mydb = myclient["xiaohongshu"]
mycol = mydb["notes2"]
myquery = {}
mydoc = mycol.find(myquery)

for x in mydoc:
    if x['NoteView']['noteInfo']['type'] == 'normal':
        note = Note()
        note.id = x['NoteView']['noteInfo']['id']
        note.title = x['NoteView']['noteInfo']['title']
        note.type = x['NoteView']['noteInfo']['type']
        note.desc = x['NoteView']['noteInfo']['desc']
        note.likes = x['NoteView']['noteInfo']['likes']
        note.cover = x['NoteView']['noteInfo']['cover']['original'].replace('http://ci.xiaohongshu.com/','')
        note.collects = x['NoteView']['noteInfo']['collects']
        imageStr = ''
        for image in x['NoteView']['noteInfo']['images']:
            imageStr += (image['original'].replace('http://ci.xiaohongshu.com/','') + ',')
        note.images = imageStr
        note.user_id = x['NoteView']['noteInfo']['user']['id']

        # 检查msyql数据库是否含有改笔记
        checkresults = Note.objects.filter(id=note.id)
        if len(checkresults) == 0:
            note.save()
        else:
            print('已存在！')

