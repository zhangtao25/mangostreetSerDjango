from django.db import models

class Replys(models.Model):
    reply_id = models.CharField(max_length=50,primary_key=True)
    user_id = models.CharField(max_length=50)
    reply_user_id = models.CharField(max_length=50)
    comment_id = models.CharField(max_length=50)
    reply_content = models.CharField(max_length=50)
    createtime = models.CharField(max_length=50)
    class Meta:
        db_table = "replys"

