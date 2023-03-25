from channels.generic.websocket import AsyncWebsocketConsumer
import json

class NotificationConsumer(AsyncWebsocketConsumer):

	async def connect(self):
		await self.accept()

	async def disconnect(self):
		pass

	async def receive(self, text_data):
		text_data_json = json.load(text_data)
		message = text_data_json['message']
		sender = text_data_json['sender']

		await self.send(text_data=json.dumps({
				'message':message,
				'sender':sender
			}))