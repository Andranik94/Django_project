from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    def ___str___(self):
        #db_colum = "{}{}".format(self.title,self.description)
        return self.title