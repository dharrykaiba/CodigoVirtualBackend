# Generated by Django 3.1.3 on 2020-11-20 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0003_registromodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='canchamodel',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='clientemodel',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='localmodel',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='registromodel',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='tipocanchamodel',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='tipoclientemodel',
            name='estado',
            field=models.BooleanField(default=True),
        ),
    ]