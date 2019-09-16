from django.db import models

class Follows(models.Model):
    follow_id = models.CharField(max_length=50,primary_key=True)
    user_id = models.CharField(max_length=50)
    follow_user_id = models.CharField(max_length=50)
    createtime = models.CharField(max_length=50)
    class Meta:
        db_table = "follows"

