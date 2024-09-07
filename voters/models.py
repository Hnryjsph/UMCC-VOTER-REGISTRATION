from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Voter(models.Model):
    name = models.CharField(max_length=255)
    image = CloudinaryField('image') # Stores images in MEDIA_ROOT/voter_images
    registered_by = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the user who registered the voter
    registered_at = models.DateTimeField(auto_now_add=True)  # Automatically adds timestamp of registration
    has_voted = models.BooleanField(default=False)  # Indicates if the voter has voted

    def __str__(self):
        return self.name
