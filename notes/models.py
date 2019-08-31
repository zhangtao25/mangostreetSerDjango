from django.db import models

class Notes(models.Model):
    id = models.CharField(max_length=50,primary_key=True)
    title = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)
    likes = models.IntegerField()
    cover = models.CharField(max_length=50)
    user_id = models.CharField(max_length=50)
    collects = models.IntegerField()
    images = models.CharField(max_length=50)
    class Meta:
        db_table = "notes"
