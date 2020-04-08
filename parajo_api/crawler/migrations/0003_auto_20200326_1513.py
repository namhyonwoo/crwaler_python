# Generated by Django 3.0.4 on 2020-03-26 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0002_carinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarBrand',
            fields=[
                ('seq', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default=None, max_length=50)),
            ],
            options={
                'db_table': 'car_category_brand',
            },
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('seq', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('brand', models.IntegerField(default=None)),
            ],
            options={
                'db_table': 'car_category_model',
            },
        ),
        migrations.CreateModel(
            name='CarModelDetail',
            fields=[
                ('seq', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default=None, max_length=50)),
                ('model', models.IntegerField(default=None)),
            ],
            options={
                'db_table': 'car_category_model_detail',
            },
        ),
        migrations.DeleteModel(
            name='Furits',
        ),
        migrations.RemoveField(
            model_name='carinfo',
            name='id',
        ),
        migrations.AddField(
            model_name='carinfo',
            name='price',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='carinfo',
            name='seq',
            field=models.AutoField(default=None, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='carinfo',
            name='accident',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='carinfo',
            name='carid',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='carinfo',
            name='info',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='carinfo',
            name='site',
            field=models.CharField(default=None, max_length=20),
        ),
    ]