import datetime

from django.db import models
from django.conf import settings
from django.db.models.functions import ExtractWeek
from django.utils import timezone
from datetime import datetime


class Choice(models.Model):

    choice_text = models.CharField(max_length=20)

    def __str__(self):
        return self.choice_text


class Action(models.Model):

    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, default=1)
    action_text = models.CharField(max_length=250)
    pub_date = models.IntegerField('week published')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, default=0)
    goodbad = models.BooleanField(default= False)

    # @property
    # def is_this_week(self):
    #     today = datetime.today()
    #     return today.strftime("%U") == self.pub_date.strftime("%U")

    def __str__(self):
        return self.action_text
