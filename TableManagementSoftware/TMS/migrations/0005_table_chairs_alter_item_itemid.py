# Generated by Django 5.1.1 on 2024-10-14 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TMS', '0004_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='chairs',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='itemID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]