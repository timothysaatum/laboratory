from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer

from .models import Database

@receiver(post_save, sender=Database)
def send_database_notification(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        message = f"New database '{instance.name}' created!"
        asyncio.new_event_loop().run_until_complete(channel_layer.group_send('database_group', {
            'type': 'database_created',
            'message': message
        }))
