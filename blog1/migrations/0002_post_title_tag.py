# Generated by Django 4.0 on 2022-12-23 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='CrazyAwsomeBlog', max_length=50),
        ),
    ]
