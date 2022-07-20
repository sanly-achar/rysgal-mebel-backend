from django.db import models
from django.contrib.auth.models import User
from api.utils import get_random_string

def upload_to(instance, filename):
    rand = get_random_string()
    return 'profiles/{rand}{filename}'.format(rand=rand, filename=filename)

class Profile(models.Model):
    REGION = [
        (1, "Asgabat"),
        (2, "Ahal"),
        (3, 'Balkan'),
        (4, 'Dashoguz'),
        (5, 'Lebap'),
        (6, 'Mary')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    image = models.ImageField(("Image"), upload_to=upload_to, default="prifiles")
    mobile = models.CharField(max_length=255, null=True, blank=True)
    fullname = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=128, null=True, blank=True)
    region = models.IntegerField(choices=REGION, default=1)
    address_line_1 = models.CharField(max_length=255, null=True, blank=True)
    address_line_2 = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user.username)
    
    class Meta:
        ordering = ['-created_at']