# Generated by Django 3.1.5 on 2021-01-26 04:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Emergency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(default='', max_length=2000)),
                ('priority', models.CharField(choices=[('1', 'Info'), ('2', 'Warning'), ('3', 'Danger')], default='1', max_length=4)),
                ('enabled', models.BooleanField()),
                ('date_created', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info_contents', models.CharField(default='uh oh: no information found in class Information(models.Model) for info_contents = models.CharField. Check your internet connection and try again. (Please fill something in Django Admin!) (Errno #2) ', max_length=20000)),
                ('manage_contents', models.CharField(default='uh oh: no information found in class Information(models.Model) for manage_contents = models.CharField. Check your internet connection and try again. (Please fill something in Django Admin!) (Errno #2) ', max_length=20000)),
                ('date_modified', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(choices=[('OTH', 'Other'), ('MET', 'Meta'), ('WKS', 'Weekly Summary'), ('ENS', 'English Standard'), ('ENA', 'English Advanced'), ('ENX', 'English Extension 1'), ('EN2', 'English Extension 2'), ('MAS', 'Maths Standard 2'), ('MAT', 'Maths Advanced'), ('MA1', 'Maths Extension 1'), ('MA2', 'Maths Accelerated'), ('BIO', 'Biology'), ('CHE', 'Chemistry'), ('PHY', 'Physics'), ('INS', 'Investigating Science'), ('ENG', 'Engineering Studies'), ('SIC', 'Studies in Catholic Thought'), ('SOR', 'Studies of Religion I'), ('SRX', 'Studies of Religion II'), ('ECO', 'Economics'), ('BUS', 'Business Studies'), ('LST', 'Legal Studies'), ('HIA', 'Ancient History'), ('HIM', 'Modern History'), ('GEO', 'Geography'), ('PDH', 'PDHPE'), ('DRA', 'Drama'), ('VAR', 'Visual Arts'), ('MU1', 'Music 1'), ('MU2', 'Music 2'), ('FRE', 'French Continuers'), ('LAT', 'Latin Continuers'), ('JAP', 'Japanese Continuers')], default='NAS', max_length=3)),
                ('channel', models.CharField(choices=[('MAIN', 'Main channel'), ('LOWP', 'Low Priority'), ('META', 'Meta')], default='MAIN', max_length=4)),
                ('title', models.CharField(max_length=2000)),
                ('content', models.CharField(max_length=2000)),
                ('location', models.CharField(max_length=2000)),
                ('date', models.DateField()),
                ('important', models.BooleanField()),
                ('date_created', models.DateField(default=django.utils.timezone.now)),
                ('date_modified', models.DateField(default=django.utils.timezone.now)),
                ('creator', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
