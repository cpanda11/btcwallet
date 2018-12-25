# Generated by Django 2.0 on 2017-12-06 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='botuser',
            name='balance',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='botuser',
            name='language',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
