# Generated by Django 3.2 on 2021-04-30 21:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210430_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created_datetime'),
            preserve_default=False,
        ),
    ]
