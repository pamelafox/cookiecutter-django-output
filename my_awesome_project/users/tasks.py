from django.contrib.auth import get_user_model

from config import celery_app

User = get_user_model()


@celery_app.task(bind=True)
def get_users_count(self):
    """A pointless Celery task to demonstrate usage."""
    print(f"Task request: {self.request}")
    return User.objects.count()
