# Generated by Django 5.0.3 on 2024-04-15 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0009_alter_task_column'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='column',
            field=models.CharField(max_length=50),
        ),
    ]
