from django.db import models
from django.contrib.auth.models import User

class NewsUnit(models.Model):
    category = models.CharField(max_length=10, null=False)
    author = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=False)
    message = models.TextField(null=False)
    pubtime = models.DateTimeField(auto_now=True) #自動取得目前時間
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title

