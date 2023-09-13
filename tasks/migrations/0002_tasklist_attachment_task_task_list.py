# Generated by Django 4.2.4 on 2023-09-09 20:50

from django.db import migrations, models
import django.db.models.deletion
import tasks.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_house'),
        ('house', '0001_initial'),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('completed_on', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('NOT_COMPLETE', 'Not Completed'), ('COMPLETE', 'Completed')], default='NOT_COMPLETE', max_length=125)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lists', to='users.profile')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lists', to='house.house')),
            ],
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('data', models.FileField(upload_to=tasks.models.GenerateAttachmentFilePath())),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='tasks.task')),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='task_list',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='tasks.tasklist'),
            preserve_default=False,
        ),
    ]
