# Generated by Django 4.2.11 on 2024-04-14 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_checkboxdata_user_userinput_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinput',
            old_name='taskNumber',
            new_name='task_number',
        ),
    ]
