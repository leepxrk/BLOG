from django.db import models

# Create your models here.

class Qusetion(models.Model):
    qusetion_text = models.Charfield(max_length = 200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    qusetion = models.Foreignkey(Qusetion)
    Choice_text = models.Charfield(max_length = 200)
    votes = models.IntegerField(default = 0)
