from taskify.profileApp.models import UserProfile
from django.conf import settings
from django.contrib.auth import get_user_model

from django.db.models.signals import post_save
from django.dispatch import receiver

from ..profileApp.email_utils import send_email_with_template

UserModel = get_user_model()


def send_successful_registration_email(user):
    context = {
        'user': user,
    }
    send_email_with_template(
        subject='Registration greetings',
        template_name='profile/email-greeting.html',
        context=context,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=(user.email,)
    )


@receiver(post_save, sender=UserModel)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        send_successful_registration_email(instance)
