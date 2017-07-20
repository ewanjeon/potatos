from __future__ import unicode_literals
from django.db import models


class Tblaccount(models.Model):
    aid = models.AutoField(primary_key=True)
    id = models.CharField(unique=True, max_length=45)
    pwd = models.CharField(max_length=200)
    email = models.CharField(unique=True, max_length=200)
    name = models.CharField(max_length=45)
    pfpic = models.CharField(db_column='pfPic', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    regdate = models.DateTimeField(db_column='regDate', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'tblAccount'
        unique_together = (('aid', 'id', 'email'),)
