from django.db import models

class Poll(models.Model):
	question = models.TextField(max_length=200)
	option_one = models.CharField(max_length=80)
	option_two = models.CharField(max_length=80)
	option_three = models.CharField(max_length=80)
	option_one_count = models.IntegerField(default=0)
	option_two_count = models.IntegerField(default=0)
	option_three_count = models.IntegerField(default=0)
