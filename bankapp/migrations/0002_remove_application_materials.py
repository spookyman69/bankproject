# Generated by Django 4.1.4 on 2023-11-06 04:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='materials',
        ),
    ]
