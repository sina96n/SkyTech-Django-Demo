# Generated by Django 3.2.5 on 2021-09-23 13:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_attendant',
            field=models.BooleanField(default=False, help_text='Designates whether the user is attendant.'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_operator',
            field=models.BooleanField(default=False, help_text='Designates whether the user is operator.'),
        ),
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operator_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Attendant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]