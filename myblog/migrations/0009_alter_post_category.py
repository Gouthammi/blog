# Generated by Django 3.2.7 on 2021-09-17 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0008_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='jobs', max_length=255),
        ),
    ]