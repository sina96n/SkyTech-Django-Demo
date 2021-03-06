# Generated by Django 3.2.5 on 2021-09-25 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_rename_attendant_attendant_attendant_user'),
        ('meeting', '0007_meeting_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='attendants',
            field=models.ManyToManyField(blank=True, default=None, to='user.Attendant'),
        ),
    ]
