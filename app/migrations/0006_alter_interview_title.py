# Generated by Django 4.0 on 2021-12-20 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_interview_participant_delete_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interview',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]