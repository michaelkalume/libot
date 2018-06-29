from django.http import HttpResponse
from django.conf import settings
from botapi.models import Chat, Message

import telepot

BOT_TOKEN = settings.BOT_TOKEN
BOT = telepot.Bot(BOT_TOKEN)

def getBotDetails(request):
	bot_details = BOT.getMe()
	if(bot_details['username'] == "mikakibot"):
		return HttpResponse("mikaki")
	return HttpResponse("unmikaki")

def getUpdates(request):
	db_count = Message.objects.all().count()
	updates = BOT.getUpdates()
	updates_length = len(updates)
	if updates_length < db_count:

	return HttpResponse(updates)


# powerful-stream-43739
