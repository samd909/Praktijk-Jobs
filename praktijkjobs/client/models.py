from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    STATUS_CHOICES = (
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('closed', 'Closed'),
    )
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    deadline = models.DateTimeField(null=True, blank=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at'] 



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add custom fields here
    permission = models.IntegerField(default=1)
    bio = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    kvk = models.CharField(max_length=50, default="Geen KVK")
    city = models.CharField(max_length=50, blank=True, null=True)
    
    pc = models.CharField(max_length=10, blank=True)
    street = models.CharField(max_length=100, blank=True)



    def __str__(self):
        return self.user.username



