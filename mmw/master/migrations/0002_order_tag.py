# Generated by Django 2.2.1 on 2019-05-27 04:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='master.Tag'),
        ),
    ]
