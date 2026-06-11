import json
import datetime
from decimal import Decimal
from uuid import UUID

from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from django.forms.models import model_to_dict

from accounts.middleware import get_current_user, get_current_ip
from accounts.models import User
from employees.models import Employee
from leaves.models import LeaveRequest
from payroll.models import PayrollDetail
from assets.models import Asset
from expenses.models import ExpenseRequest
from evaluations.models import PerformanceEvaluation
from audit_logs.models import AuditLog

# List of models we track
TRACKED_MODELS = [
    User, Employee, LeaveRequest, PayrollDetail, Asset, ExpenseRequest, PerformanceEvaluation
]

class AuditJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (Decimal, UUID)):
            return str(obj)
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()
        return super().default(obj)

def serialize_instance(instance):
    """
    Safely serialize a Django model instance to a JSON-compatible dict.
    """
    try:
        data = model_to_dict(instance)
        # Convert non-serializable fields to string/iso strings
        serialized = json.dumps(data, cls=AuditJSONEncoder)
        return json.loads(serialized)
    except Exception:
        return {}

# 1. Capture Pre-Save (for UPDATEs to see old state)
@receiver(pre_save)
def audit_pre_save_handler(sender, instance, **kwargs):
    if sender not in TRACKED_MODELS:
        return
        
    if instance.pk:
        try:
            # Query db for existing data before edit
            original = sender.objects.get(pk=instance.pk)
            instance._old_data_dict = serialize_instance(original)
        except sender.DoesNotExist:
            instance._old_data_dict = None
    else:
        instance._old_data_dict = None

# 2. Capture Post-Save (CREATEs & UPDATEs)
@receiver(post_save)
def audit_post_save_handler(sender, instance, created, **kwargs):
    if sender not in TRACKED_MODELS:
        return

    action = "CREATE" if created else "UPDATE"
    new_data = serialize_instance(instance)
    old_data = getattr(instance, "_old_data_dict", None)

    # Exclude passwords from user log
    if sender == User:
        if "password" in new_data: del new_data["password"]
        if old_data and "password" in old_data: del old_data["password"]

    user = get_current_user()
    ip = get_current_ip()

    AuditLog.objects.create(
        user=user,
        action=action,
        model_name=sender.__name__,
        object_id=str(instance.pk),
        old_data=old_data,
        new_data=new_data,
        ip_address=ip
    )

# 3. Capture Post-Delete
@receiver(post_delete)
def audit_post_delete_handler(sender, instance, **kwargs):
    if sender not in TRACKED_MODELS:
        return

    old_data = serialize_instance(instance)
    if sender == User and "password" in old_data:
        del old_data["password"]

    user = get_current_user()
    ip = get_current_ip()

    AuditLog.objects.create(
        user=user,
        action="DELETE",
        model_name=sender.__name__,
        object_id=str(instance.pk),
        old_data=old_data,
        new_data=None,
        ip_address=ip
    )
