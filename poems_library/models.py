from django.db import models

class Poem(models.Model):
    title = models.CharField()
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.title
    
    
    
    