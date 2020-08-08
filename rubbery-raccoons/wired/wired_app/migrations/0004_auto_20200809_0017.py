# Generated by Django 3.0.8 on 2020-08-09 00:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wired_app', '0003_merge_20200808_2110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='publication_date',
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(null=True, on_delete=models.SET(None), to=settings.AUTH_USER_MODEL),
        ),
    ]