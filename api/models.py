from django.db import models
import random
import string

def generate_unique_code():
    length = 6
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length)) # k is the length of the string
        if Room.objects.filter(code=code).count() == 0:
            break
    return code

# Create your models here.
class Room(models.Model):
    code = models.CharField(max_length=8, default=generate_unique_code, unique=True)
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now_add=True, this will automatically add the current date and time when the object is created

    # def check_the_code(self):
    #     if self.code == "":
    #         self.code = self.generate_the_code()
    #     super().save()