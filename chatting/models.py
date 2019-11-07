from django.db import models

class chatting(models.Model):
    chat = models.TextField(max_length=100)
    pub_date = models.DateTimeField('date published')

def summary(self):
    return self.body[:100]

def __str__(self):
    return self.chat