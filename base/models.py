from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.
class Task(models.Model):
    #Foreign Key = ManyToOneField, One user many other fields
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank = True, null = True) 
    title = models.CharField(max_length = 100)
    description =  models.TextField(null= True, blank = True)
    complete = models.BooleanField(default = False)
    duedate = models.DateTimeField(auto_now=False, auto_now_add=False, blank = True, null = True)

    def __str__(self):
        return self.title

    #Meta is the inner class of a model class. It is optional
    class Meta:
        #Ordering decides the order of the model fields
        #This enables each completed task to go to the bottom automatically
        ordering = ['complete']
        
