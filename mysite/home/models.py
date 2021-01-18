from django.db import models

# Create your models here.
class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=120)
    message=models.TextField(max_length=255)
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return 'Name:  '+self.name+' ---Message:  '+self.message+'--- Email: '+self.email
 

