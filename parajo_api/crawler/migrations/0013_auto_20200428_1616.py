# Generated by Django 3.0.4 on 2020-04-28 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0012_auto_20200427_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='carinfo',
            name='catg_grade_id',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='cargrade',
            name='modelDetail',
            field=models.ForeignKey(db_column='modelDetail', on_delete=django.db.models.deletion.PROTECT, to='crawler.CarModelDetail'),
        ),
    ]
