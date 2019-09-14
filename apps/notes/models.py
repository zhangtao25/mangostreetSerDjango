from django.db import models
from django.contrib.auth.models import AbstractUser
from db.base_model import BaseModel
from apps.users.models import *

class Notes(models.Model):
    id = models.CharField(max_length=50,primary_key=True)
    title = models.CharField(max_length=50)
    type = models.CharField(max_length=50,default="normal")
    desc = models.CharField(max_length=50)
    likes = models.IntegerField(default=0)
    cover = models.CharField(max_length=50,)
    user_id = models.CharField(max_length=50)
    collects = models.IntegerField(default=0)
    images = models.CharField(max_length=50)
    n_user = models.ForeignKey(User,on_delete=models.CASCADE)
    # is_delete=models.BooleanField(max_length=2,default=False)
    class Meta:
        db_table = "notes"

