# 引用新的模块
import datetime


# 方法
from django.db import models
from django.utils import timezone


# Create your models here.

class Qusetion(models.Model):
    qusetion_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.qusetion_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)


class Choice(models.Model):
    qusetion = models.ForeignKey(Qusetion)
    Choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)
    def __str__(self):
        return self.Choice_text

