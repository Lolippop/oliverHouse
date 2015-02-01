from django.db import models

# Create your models here.

# class Article(models.Model):
#     name = models.CharField(max_length=128,unique = True)
#     def __unicode__(self):
#         return self.name

class Article(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    createTime = models.DateTimeField(null=False)
    content = models.TextField(null=False)
    url = models.TextField(null=False)