from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)
    avatar_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_profile(self):
        return self

    # def __str__(self):
    #     return f"Profile of {self.user.username}"

# Extend the User model with a profile property
def get_profile(self):
    return UserProfile(self).get_profile()

pr = get_profile(User)
print("before user add to class")
print(pr)
User.add_to_class('profile', property(get_profile))
print("after user add to class")
