# Generated by Django 2.2.22 on 2021-05-12 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StockTickers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RegNum', models.IntegerField()),
                ('Name', models.CharField(max_length=100)),
                ('CGPA', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='StockTicks',
        ),
    ]
