from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=256, verbose_name='Title')
    description = models.TextField(null=True, blank=True, verbose_name="description")
    complete =  models.BooleanField(default=False, verbose_name="Complete")
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    

    class Meta:
        ordering=['complete']
