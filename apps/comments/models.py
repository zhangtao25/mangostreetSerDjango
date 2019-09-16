from django.db import models

class Comments(models.Model):
    comment_id = models.CharField(max_length=50,primary_key=True)
    user_id = models.CharField(max_length=50)
    note_id = models.CharField(max_length=50)
    comment_content = models.CharField(max_length=50)
    createtime = models.CharField(max_length=50)
    class Meta:
        db_table = "comments"

