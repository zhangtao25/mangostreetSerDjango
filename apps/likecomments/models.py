from django.db import models

class Likecomments(models.Model):
    likecomment_id = models.CharField(max_length=50,primary_key=True)
    user_id = models.CharField(max_length=50)
    comment_id = models.CharField(max_length=50)
    createtime = models.CharField(max_length=50)
    class Meta:
        db_table = "likecomments"

