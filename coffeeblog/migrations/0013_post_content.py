# Generated by Django 3.2.13 on 2022-05-18 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffeeblog', '0012_remove_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(null=True),
        ),
    ]