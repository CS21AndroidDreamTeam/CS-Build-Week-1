# Generated by Django 2.2.5 on 2019-09-25 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_item_origin'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='originid',
            field=models.IntegerField(default=0),
        ),
    ]
