# Generated by Django 3.1.1 on 2020-09-23 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blackboard', '0002_blackboard_blackboardmembership'),
    ]

    operations = [
        migrations.AddField(
            model_name='blackboardmembership',
            name='last_read',
            field=models.DateTimeField(blank=True, help_text='The last time the user viewed this blackboard.', null=True),
        ),
        migrations.AddField(
            model_name='blackboardmembership',
            name='last_write',
            field=models.DateTimeField(blank=True, help_text='The last time the user modified this blackboard.', null=True),
        ),
    ]
