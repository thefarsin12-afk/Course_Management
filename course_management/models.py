from django.db import models

class Course(models.Model):

    title =  models.CharField(max_length=200)

    language = models.CharField(max_length=200)

    description = models.TextField()

    duration = models.CharField()

    trainer = models.CharField(max_length=200)

    price = models.DecimalField(max_digits=10,decimal_places=2)

    cover_picture = models.ImageField(upload_to="cover_pics",null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
          self.title




    

