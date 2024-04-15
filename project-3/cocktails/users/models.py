from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Users(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
class CheckboxData(models.Model):
    checkbox1 = models.BooleanField(default=False)
    checkbox2 = models.BooleanField(default=False)
    checkbox3 = models.BooleanField(default=False)
    checkbox4 = models.BooleanField(default=False)
    checkbox5 = models.BooleanField(default=False)
    checkbox6 = models.BooleanField(default=False)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

class UserInput(models.Model):
    text = models.TextField()
    task_number = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    def __str__(self):
        return self.text





