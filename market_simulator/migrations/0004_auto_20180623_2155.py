# Generated by Django 2.0.6 on 2018-06-23 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market_simulator', '0003_auto_20180623_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='symbol',
            name='sector',
            field=models.CharField(choices=[('cmpsoft', 'Computers - Software'), ('finhouse', 'Finance - Housing')], max_length=100),
        ),
        migrations.AlterUniqueTogether(
            name='dailysymboldata',
            unique_together={('symbol', 'date', 'data_souce')},
        ),
    ]