# Generated by Django 4.2.4 on 2023-12-22 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0002_poll_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='end_date',
            field=models.DateTimeField(blank=True, help_text='Poll ending date and time', null=True),
        ),
        migrations.AddField(
            model_name='poll',
            name='recipient_emails',
            field=models.TextField(blank=True, help_text='Enter email addresses separated by commas', null=True),
        ),
    ]
