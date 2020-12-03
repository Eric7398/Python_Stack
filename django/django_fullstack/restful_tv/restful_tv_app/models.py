from django.db import models
from datetime import date

class TVshowManager(models.Manager):
    @property
    def is_past_due(self):
        if date.today() > self.date:
            errors = {}  
            errors["release"] = "Release date must be before current date!"
    def basic_validator(self, post_data):
        errors = {}        
        
        if len(post_data['title']) < 5:
            errors["title"] = "TVshow title should be at least 5 characters"
            
            
        if len(post_data['desc']) > 0 and len(post_data['desc']) < 11:
            errors["desc"] = "TVshow description should be at least 10 characters"
            
        
        
        return errors



class TVshow(models.Model):
    title = models.CharField(max_length=255)
    release = models.DateField()
    desc = models.TextField(default = "No Description!")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = TVshowManager()
    

class NetworkManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}       
        
        if len(post_data['name']) < 3:
            errors["name"] = "Network name should be at least 3 characters"
    
class Network(models.Model):
    name = models.CharField(max_length=255)
    shows = models.ManyToManyField(TVshow, related_name = "networks")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = NetworkManager()
    

    