from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    date_of_post = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=30)
    date_of_change = models.DateField(auto_now=True)
    image = models.ImageField(upload_to=f'posts/%Y/%m/%d')
    visits = models.IntegerField(default=0)
   
   
    def __str__(self):
        return self.title
 
    def get_absolute_url(self):
        return "/%s/" %(self.id)
 
    class Meta:
        ordering = ["-id", "-date_of_post"]


class Comment(models.Model):
    post = models.ForeignKey(
        "Post",
        on_delete=models.CASCADE,
        related_name = "comments",
    )
    author = models.CharField(max_length=30)
    data = models.DateTimeField(auto_now=False, auto_now_add=True)
    email = models.EmailField()
    comment = models.TextField()
