from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class eventlist(models.Model):
    id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=100)
    data = models.CharField(max_length=500)
    date = models.DateField()
    location = models.CharField(max_length=35)
    image = models.ImageField(upload_to="images/")
    is_liked = models.ManyToManyField(User)

    def __str__(self):
        return self.event_name
