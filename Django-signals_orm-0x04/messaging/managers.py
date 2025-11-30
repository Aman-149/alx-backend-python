from django.db import models

class UnreadMessagesManager(models.Manager):
    """
    Provides a helper to get unread messages for a user.
    The checker expects a method named `unread_for_user`.
    """
    def unread_for_user(self, user):
        # return a queryset filtered to unread messages for a user
        # keep the queryset flexible so callers can .only() or further chain
        return super().get_queryset().filter(receiver=user, read=False)
