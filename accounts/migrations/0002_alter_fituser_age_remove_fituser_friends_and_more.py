# Generated by Django 5.1.5 on 2025-04-17 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fituser',
            name='age',
            field=models.PositiveIntegerField(default=20),
        ),
        migrations.RemoveField(
            model_name='fituser',
            name='friends',
        ),
        migrations.AlterField(
            model_name='fituser',
            name='weight',
            field=models.PositiveIntegerField(default=160),
        ),
        migrations.AddField(
            model_name='fituser',
            name='friends',
            field=models.TextField(blank=True),
        ),
    ]
