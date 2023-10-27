from django.db import models
from django.contrib.auth.models import User

# Create your models here.

BLOG_STATUS = [
    ('A', "Active"),
    ('D', "Draft"),
    ('IA', 'Inactive')
]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to="images/")
    phone = models.PositiveBigIntegerField()


class Blog(models.Model):
    title = models.CharField(max_length=15)
    content = models.TextField(help_text="Enter the Blog Content")
    image = models.ImageField(upload_to="images/blog", null=True)
    status = models.CharField(max_length=2, choices=BLOG_STATUS)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at', '-created_at']
