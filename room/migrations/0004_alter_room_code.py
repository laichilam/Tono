# Generated by Django 4.1.6 on 2023-02-22 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0003_alter_room_created_at_alter_room_modified_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='code',
            field=models.CharField(max_length=8, unique=True),
        ),
    ]
