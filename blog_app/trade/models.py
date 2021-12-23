from django.db import models


class Trade(models.Model):

    date_time = models.DateTimeField('Y-m-d')
    
