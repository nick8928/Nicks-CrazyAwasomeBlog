# Generated by Django 4.0 on 2022-12-28 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog1', '0005_post_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]
