# Generated by Django 3.2.7 on 2021-09-15 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='LaVaNyA BLooog!', max_length=255),
        ),
    ]
