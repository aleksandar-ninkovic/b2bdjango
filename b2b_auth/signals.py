from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile
from repositories.mongo_repository import MongoRepository

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        print("Profile created in Django ORM!")

        # Create the UserProfile in MongoDB via the repository
        mongo_repo = MongoRepository()
        mongo_repo.insert_one("user_profiles",{
            "user": instance.username,
            "bio": "",
            "avatar_url": "",
            "created_at": instance.date_joined.isoformat(),
            "updated_at": instance.date_joined.isoformat()
        })
        print("Profile created in MongoDB!")
