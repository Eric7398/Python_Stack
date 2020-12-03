from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    State = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Ninja(models.Model):
    dojoid = models.ForeignKey(Dojo, related_name="ninjas", on_delete = models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    #>>> A = Dojo.objects.create(name = "dojoA", city = "A", State = "A")
    #>>> B = Dojo.objects.create(name = "dojoB", city = "B", State = "B")
    #>>> C = Dojo.objects.create(name = "dojoC", city = "C", State = "C")
    
    
    # Ninja.objects.create(first_name = "John", last_name = "Wick", dojoid = A)
    # Ninja.objects.create(first_name = "Eric", last_name = "Wang", dojoid = A)
    # Ninja.objects.create(first_name = "Krystal", last_name = "Huang", dojoid = A)