# Generated by Django 3.1.5 on 2021-06-30 08:29

import board.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0010_post_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=board.models.Post.file_path),
        ),
    ]
