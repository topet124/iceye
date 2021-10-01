from django.db import models

# Create your models here.


class Entry(models.Model):
    text = models.TextField()
    name = models.CharField(max_length=200, null=True)
    place = models.CharField(max_length=200, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'entries'


class List_name(models.Model):
    text = models.TextField()
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return 'Names  #{}'.format(self.id)

    class Meta:
        verbose_name_plural = 'Lists'
