# Generated by Django 2.2.7 on 2019-11-25 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0005_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]