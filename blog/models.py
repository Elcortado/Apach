from django.db import models

# Create your models here.

class Comment(models.Model):
    
    name = models.CharField(max_length= 100, null=False)
    feedback = models.CharField(max_length=1000, null=True)
    score = models.IntegerField(default=3)
    date = models.DateField(null=True)
    
    def __str__(self):
        return f'{self.name} \n{self.feedback}'


