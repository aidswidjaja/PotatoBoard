# Generated by Django 3.1.5 on 2021-06-29 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0006_auto_20210130_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='subject',
            field=models.CharField(choices=[('OTH', 'Other'), ('MET', 'Meta'), ('WKS', 'Weekly Summary'), ('ENS', 'English Standard'), ('ENA', 'English Advanced'), ('ENX', 'English Extension 1'), ('EN2', 'English Extension 2'), ('MAS', 'Maths Standard 2'), ('MAT', 'Maths Advanced'), ('MA1', 'Maths Extension 1'), ('MA2', 'Maths Accelerated'), ('BIO', 'Biology'), ('CHE', 'Chemistry'), ('PHY', 'Physics'), ('INS', 'Investigating Science'), ('ENG', 'Engineering Studies'), ('SIC', 'Studies in Catholic Thought'), ('SOR', 'Studies of Religion I'), ('SRX', 'Studies of Religion II'), ('ECO', 'Economics'), ('BUS', 'Business Studies'), ('LST', 'Legal Studies'), ('HIA', 'Ancient History'), ('HIM', 'Modern History'), ('GEO', 'Geography'), ('PDH', 'PDHPE'), ('DRA', 'Drama'), ('VAR', 'Visual Arts'), ('MU1', 'Music 1'), ('MU2', 'Music 2'), ('FRE', 'French Continuers'), ('LAT', 'Latin Continuers'), ('JAP', 'Japanese Continuers')], default='NAS', help_text='"Other" will not provide a title automatically to any post you push', max_length=3),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(help_text='e.g English Extension 1, Athletics Carnival - leave blank if using Subject.', max_length=2000),
        ),
    ]
