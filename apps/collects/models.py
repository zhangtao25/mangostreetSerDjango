from django.db import models

class Collects(models.Model):
    collect_id = models.CharField(max_length=50,primary_key=True)
    user_id = models.CharField(max_length=50)
    note_id = models.CharField(max_length=50)
    createtime = models.CharField(max_length=50)
    class Meta:
        db_table = "collects"

