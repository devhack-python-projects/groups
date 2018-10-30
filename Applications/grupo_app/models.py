from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20)

class Group(models.Model):
    name = models.CharField(max_length= 20)
    author = models.OneToOneField(User, on_delete=models.CASCADE, related_name= "author")
    description = models.CharField(max_length= 100)
    members = models.ManyToManyField(User, related_name= "members")

class Publication(models.Model):
    text = models.TextField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

class Comment(models.Model):
    text = models.TextField()
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
