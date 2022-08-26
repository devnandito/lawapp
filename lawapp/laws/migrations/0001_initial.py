# Generated by Django 4.0.6 on 2022-07-26 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Law',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created_at')),
                ('update_at', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='update_at')),
                ('title', models.CharField(max_length=500)),
            ],
            options={
                'ordering': ['-created_at', '-update_at'],
                'get_latest_by': 'created_at',
                'abstract': False,
            },
        ),
    ]
