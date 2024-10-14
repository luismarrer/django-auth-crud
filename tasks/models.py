from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
	user = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	date_completed = models.DateTimeField(null=True, blank=True)
	important = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title + '- ' + self.user.username