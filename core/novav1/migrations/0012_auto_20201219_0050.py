# Generated by Django 3.1.2 on 2020-12-18 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novav1', '0011_auto_20201217_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ref_code',
            field=models.CharField(default='LDZVARM2Y1GBH7BJRBJW', max_length=20),
        ),
    ]