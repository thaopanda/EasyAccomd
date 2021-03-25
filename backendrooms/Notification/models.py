from django.db import models
from Account.models import MyUser

class NotificationManager(models.Manager):
    def CreateNotification(self, user, message):
        notification = self.model(user=user, message=message)
        notification.save(using = self._db)

class Notification(models.Model):
    user = models.ForeignKey(MyUser, related_name='notified_user', on_delete=models.CASCADE)
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    objects = NotificationManager()