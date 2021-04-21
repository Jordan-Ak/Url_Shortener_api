from django.db import models
from string import ascii_letters, digits
from random import choices

from .admin_variables import num_random_strings, HOST_URL

# Create your models here.

class Link(models.Model):
    input_link = models.URLField()
    short_link = models.URLField(blank = True, null = True, read_only = True,)
    when_created = models.DateTimeField(auto_add_now = True)

#user makes custom short url idea
    
    def random_generator(self):
        random_strings = ''.join(choices(ascii_letters + digits,k=num_random_strings)) #Inputting random cha
        random_link = HOST_URL + random_strings

        if not Link.objects.get(short_link = self.random_link).exists():
            return random_link
        
        else:
            random_generator() #I put recursion in cool!
    
    def save(self, *args, **kwargs):
        if not self.short_link:
            link = self.random_generator()
            self.short_link = link
        return super().save(*args, **kwargs)
