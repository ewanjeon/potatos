from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from account.models import Tblaccount


class Tbldevnews(models.Model):
    cid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=45)
    frontimage = models.CharField(max_length=500, blank=True, null=True)
    summary = models.CharField(max_length=45, blank=True, null=True)
    content = models.TextField()
    writer = models.ForeignKey(Tblaccount,related_name='writer')
    regdate = models.DateTimeField(db_column='regDate')  # Field name made lowercase.

    def publish(self):
        self.regdate = timezone.now()
        self.save()


    def __str__(self):
        return self.title

    class Meta:
        managed = False
        db_table = 'tblDevNews'

