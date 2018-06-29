# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Chat(models.Model):
	chat_id = models.IntegerField()
	first_name = models.CharField(max_length=200, blank=False, null=False)
	last_name = models.CharField(max_length=200, blank=False, null=False)
	chat_type = models.CharField(max_length=20, blank=False, null=False)
	username = models.CharField(max_length=50, blank=False, null=False)

	class Meta:
		ordering = ['chat_id']
		db_table = 'chats'


class Message(models.Model):
	chat_id = models.ForeignKey(Chat, on_delete=models.CASCADE)
	message_id = models.IntegerField(primary_key=True)
	date = models.DateTimeField()
	from_first_name = models.CharField("senders first name", max_length=200, blank=False, null=False)
	from_last_name = models.CharField("senders last name", max_length=200, blank=False, null=False)
	from_last_name = models.CharField("senders user name", max_length=50, blank=False, null=False)
	message_type = models.CharField(max_length=20)
	text = models.CharField(max_length=500)
	update_id = models.IntegerField()
	is_bot = models.BooleanField()

	class Meta:
		ordering = ['message_id']
		db_table = 'messages'
		get_latest_by = ['-priority', 'date']
