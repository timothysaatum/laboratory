from channels.generic.websocket import AsyncWebsocketConsumer
import asyncio

class DatabaseConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('database_group', self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard('database_group', self.channel_name)

    async def database_created(self, event):
        await self.send(text_data=event['message'])
