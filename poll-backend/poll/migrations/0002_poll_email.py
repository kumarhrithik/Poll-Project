# Generated by Django 4.2.4 on 2023-12-22 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
