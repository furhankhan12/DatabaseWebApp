# Generated by Django 3.0.5 on 2020-04-25 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoosworkinout', '0008_auto_20200425_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='workedoutat',
            name='id',
            field=models.AutoField( primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]