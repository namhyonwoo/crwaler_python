# Generated by Django 3.0.4 on 2020-09-24 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0024_auto_20200924_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='carbrand',
            name='checked',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='carmodel',
            name='checked',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='carmodeldetail',
            name='checked',
            field=models.IntegerField(default=None),
        ),
    ]