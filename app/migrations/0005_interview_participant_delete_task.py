# Generated by Django 4.0 on 2021-12-19 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('app', '0004_alter_task_starttime'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30, unique=True)),
                ('startTime', models.TimeField()),
                ('endTime', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.interview')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
