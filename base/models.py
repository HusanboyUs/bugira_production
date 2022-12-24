from django.db import models
from django.contrib.auth.models import User

class Tickets(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True) #the owner of created the ticket
    title=models.CharField(max_length=15, null=True,blank=True)
    summary=models.TextField(null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Tickets'
        verbose_name_plural='Tickets'
        ordering=['-created',]

    def __str__(self):
        return self.title 