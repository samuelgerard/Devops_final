# Generated by Django 3.2.9 on 2021-12-06 01:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('core', '0008_remove_dyaduser_dyad_group'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DyadGroup',
        ),
    ]
