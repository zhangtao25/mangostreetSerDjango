from apps.users.models import *

class Notes(models.Model):
    id = models.CharField(max_length=50,primary_key=True)
    title = models.CharField(max_length=50)
    type = models.CharField(max_length=50,default="normal")
    desc = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)
    cover = models.CharField(max_length=50,)
    user_id = models.CharField(max_length=50)
    collects = models.IntegerField(default=0)
    images = models.CharField(max_length=255)
    n_user = models.ForeignKey(Users,on_delete=models.CASCADE)
    # is_delete=models.BooleanField(max_length=2,default=False)
    class Meta:
        db_table = "notes"


class Likes(models.Model):
    like_id = models.CharField(max_length=20,primary_key=True)
    user_id = models.CharField(max_length=20)
    note_id = models.CharField(max_length=20)


class Collects(models.Model):
    collect_id = models.CharField(max_length=20,primary_key=True)
    user_id = models.CharField(max_length=20)
    note_id = models.CharField(max_length=20)
