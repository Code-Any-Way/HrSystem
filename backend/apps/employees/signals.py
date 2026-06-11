from django.db.models.signals import post_delete
from django.dispatch import receiver
from employees.models import Employee

@receiver(post_delete, sender=Employee)
def delete_related_user(sender, instance, **kwargs):
    """
    Remove the associated Django user credentials when an employee record is removed.
    """
    try:
        if instance.user:
            instance.user.delete()
    except Exception:
        pass
