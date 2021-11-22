# Generated by Django 2.2.19 on 2021-04-03 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StockTicks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('INFY', models.FloatField()),
                ('HEG', models.FloatField()),
                ('TCS', models.FloatField()),
                ('ALANKIT', models.FloatField()),
                ('SBI', models.FloatField()),
                ('TATAMOTORS', models.FloatField()),
                ('SBICARD', models.FloatField()),
                ('GLAND', models.FloatField()),
                ('UJJIVANSFB', models.FloatField()),
                ('CIPLA', models.FloatField()),
            ],
        ),
    ]
