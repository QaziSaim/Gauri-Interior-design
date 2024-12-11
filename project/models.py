from django.db import models
from django.urls import reverse


# Create your models here.
class Project(models.Model):
    # title = models.CharField(max_length=30,null=True)
    TYPE = (
        ('Sofa', 'Sofa'),
        ('Curtains', 'Curtains'),
        ('Mattress', 'Mattress'),
        ('Chairs','Chairs'),
        ('Decorators','Decorators')
    )
    type = models.CharField(max_length=30, null=True, choices=TYPE)
    # description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    # def __str__(self):
    #     return self.title

    def get_absolute_url(self):
        return reverse('project:project_detail', kwargs={
            'project_id': self.id
        })