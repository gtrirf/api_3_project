from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    photo = models.ImageField(upload_to='users/', blank=True, null=True)
    about = models.TextField(blank=True, null=True)

    joined_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.first_name