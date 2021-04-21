from django.db import models
from string import ascii_letters, digits
from random import choices
import uuid

from .admin_variables import num_random_strings, HOST_URL, custom_max_length

# Create your models here.

class Link(models.Model):
    UUID = models.UUIDField(primary_key = True, editable = False, default=uuid.uuid4)
    input_link = models.URLField()
    short_link = models.URLField(blank = True, null = True,)
    when_created = models.DateTimeField(auto_now_add = True)
    custom_link = models.CharField(blank = True, null = True, unique = True,
                                         max_length = custom_max_length,)

#user makes custom short url idea
    
    def random_generator(self):
        random_strings = ''.join(choices(ascii_letters + digits,k=num_random_strings)) #Inputting random cha
        random_link = HOST_URL +'/'+ random_strings

        try:
            Link.objects.get(short_link = random_link)
        
        except Link.DoesNotExist:
            return random_link
        
        else:
            random_generator() #I put recursion in cool!
    
    def custom_generator(self):
        custom_gen = HOST_URL + '/' + self.custom_link
        return custom_gen

    def save(self, *args, **kwargs):
        if not self.short_link and not self.custom_link:
            link = self.random_generator()
            self.short_link = link
        else:
            link = self.custom_generator()
            self.short_link = link
        return super().save(*args, **kwargs)
