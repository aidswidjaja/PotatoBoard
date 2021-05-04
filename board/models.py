from django.db import models
from django.forms import ModelForm
from django.conf import settings
from django.utils.timezone import now
from .subjects import Subject
from django.contrib.auth.models import User

# help_text attributes are customised for TYSK, you will need to change them on an external deploy

class Post(models.Model):
    subject = models.CharField(max_length=3, choices=Subject.SUBJECT_SELECTABLES, default='NAS')
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False, on_delete=models.CASCADE, null=True) # set to null=False for prod - should catch any hackers who bypass auth ig

    CHANNEL_SELECTABLES = (
        ('MAIN', 'Main channel'),
        ('LOWP', 'Low Priority'),
        ('META', 'Meta'),
    )

    channel = models.CharField(max_length=4, choices=CHANNEL_SELECTABLES, default='MAIN', help_text='Should this model be pushed to Main channel, Low Priority or Meta?')

    title = models.CharField(max_length=2000, help_text='e.g English Extension 1, Athletics Carnival')
    content = models.TextField(max_length=2000, help_text='supports GitHub-flavoured Markdown, see markdownguide.org/cheat-sheet. Not all Markdown elements (headings, horizontal line, tables) will render correctly, so stick to Discord-supported formatting please :)')
    location = models.CharField(max_length=2000, blank=True, help_text='e.g Blue Gym, W301, Sydney Olympic Park (Google Calendar only)') # Google Calendar only
    date = models.DateField(editable=True, blank=True, help_text='DD/MM/YYYY - e.g assignment due date/event date. Can be left blank. (Google Calendar and TYSK App only)', null=True) # Google Calendar and TYSK App only

    # todo: file attachments

    important = models.BooleanField(default=False, help_text='this will produce an @everyone ping on Discord and move a post to the Important channel on TYSK App') # this will produce an @everyone ping

    push_to_gcal = models.BooleanField(default=False, help_text='do you want to push this announcement to TYSK SubCal as well?') # this will produce an @everyone ping

    date_created = models.DateTimeField(default=now, editable=False)
    date_modified = models.DateTimeField(default=now, editable=False)

    # sword art online 2022 !!

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class Information(models.Model):
    info_contents = models.CharField(max_length=20000)
    manage_contents = models.CharField(max_length=20000)
    date_modified = models.DateField(default=now, editable=True)

class Emergency(models.Model):
    EMERGENCY_SELECTABLES = (
        ('1', 'Info'),
        ('2', 'Warning'),
        ('3', 'Danger'),
    )

    message = models.CharField(max_length=2000, default='')
    priority = models.CharField(max_length=4, choices=EMERGENCY_SELECTABLES, default='1')
    enabled = models.BooleanField() # is this even enabled?
    date_created = models.DateField(default=now, editable=True)

"""
python manage.py makemigrations && python manage.py migrate
"""
