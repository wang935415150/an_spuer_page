from django.db import models

class UserType(models.Model):
    caption = models.CharField(max_length=32)

class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    pwd = models.CharField(max_length=64)
    ut = models.ForeignKey(to='UserType',to_field='id',null=True,blank=True)
