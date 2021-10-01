# Generated by Django 3.2.5 on 2021-09-23 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20210923_0611'),
        ('meeting', '0002_meeting_is_open'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meeting',
            name='category',
        ),
        migrations.RemoveField(
            model_name='meeting',
            name='teacher',
        ),
        migrations.AddField(
            model_name='meeting',
            name='operator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, related_name='teacher', to='user.operator'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='meeting',
            name='attendants',
            field=models.ManyToManyField(blank=True, default=None, related_name='attendants', to='user.Attendant'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='thumbnail',
            field=models.ImageField(default='thumbnail/default/default-gray.png', upload_to='thumbnail/'),
        ),
    ]
