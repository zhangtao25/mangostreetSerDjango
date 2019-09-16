from django.db import models

class Likereplys(models.Model):
    likereply_id = models.CharField(max_length=50,primary_key=True)
    user_id = models.CharField(max_length=50)
    reply_id = models.CharField(max_length=50)
    createtime = models.CharField(max_length=50)
    class Meta:
        db_table = "likereplys"

