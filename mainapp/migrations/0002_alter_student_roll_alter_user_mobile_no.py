# Generated by Django 4.2.6 on 2024-05-14 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='roll',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='mobile_no',
            field=models.IntegerField(null=True, verbose_name='pnone no'),
        ),
    ]
