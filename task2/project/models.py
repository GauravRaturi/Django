from django.db import models

# Create your models here.
class member(models.Model):
    fname=models.CharField(max_length=50)
    email=models.EmailField(max_length=200)
    age=models.IntegerField()
    
    def __str__(self):
        return self.fname+''+self.email+''