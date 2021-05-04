# Generated by Django 3.1.5 on 2021-01-26 07:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_auto_20210126_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='info_contents',
            field=models.CharField(max_length=20000),
        ),
        migrations.AlterField(
            model_name='information',
            name='manage_contents',
            field=models.CharField(max_length=20000),
        ),
        migrations.AlterField(
            model_name='post',
            name='channel',
            field=models.CharField(choices=[('MAIN', 'Main channel'), ('LOWP', 'Low Priority'), ('META', 'Meta')], default='MAIN', help_text='Should this model be pushed to Main channel, Low Priority or Meta?', max_length=4),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(help_text='Supports Markdown formatting', max_length=2000),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(blank=True, help_text='This field is for the date on Google Calendar and TYSK App. e.g assignment due date/event date. Can be left blank.'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_created',
            field=models.DateField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_modified',
            field=models.DateField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='important',
            field=models.BooleanField(help_text='This will produce an @everyone ping on Discord and move a post to the Important channel on TYSK App'),
        ),
        migrations.AlterField(
            model_name='post',
            name='location',
            field=models.CharField(help_text='This field is for the Google Calendar location field. e.g Blue Gym, W301, Sydney Olympic Park', max_length=2000),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(help_text='Subject/Event name', max_length=2000),
        ),
    ]
