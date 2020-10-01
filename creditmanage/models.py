from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class people(models.Model):
	name=models.CharField(max_length=64)
	email=models.EmailField()
	credit=models.IntegerField()

	def __str__(self):
		return self.name

class transaction(models.Model):
	Sender=models.ForeignKey(people, on_delete=models.CASCADE, related_name="transactions")
	Receiver=models.ForeignKey(people, on_delete=models.CASCADE)
	Credit_Amount=models.IntegerField()
	Date=models.DateTimeField(default=timezone.now)
	Senderbalance=models.IntegerField()
	Receiverbalance=models.IntegerField()