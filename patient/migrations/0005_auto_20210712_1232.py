# Generated by Django 2.1.5 on 2021-07-12 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0004_auto_20210711_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
