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

    def __str__(self):
        return self.user.username


class Blog(models.Model):
    title = models.CharField(max_length=15)
    content = models.TextField(help_text="Enter the Blog Content")
    image = models.ImageField(upload_to="images/blog", null=True,blank=True,default=None)
    status = models.CharField(max_length=2, choices=BLOG_STATUS)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User,related_name="blog_likes")

    class Meta:
        ordering = ['-updated_at', '-created_at']

    def __str__(self):
        return self.title

    def num_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    comment = models.CharField(max_length=100)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment

    class Meta:
        ordering = ['-created_at']

