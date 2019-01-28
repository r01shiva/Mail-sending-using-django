from django.db import models
from django.urls import reverse


class FormM(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField()
    branch = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    mobileno = models.CharField(max_length=10)


    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.fname + '-' + str(self.id)

