# Generated by Django 4.1.3 on 2022-12-09 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emp',
            old_name='adddress',
            new_name='address',
        ),
    ]