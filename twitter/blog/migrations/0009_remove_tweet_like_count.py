# Generated by Django 3.2 on 2021-05-22 03:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_tweet_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='like_count',
        ),
    ]
