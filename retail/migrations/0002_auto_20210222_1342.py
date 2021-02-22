# Generated by Django 3.1.5 on 2021-02-22 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retail', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='buy',
            name='from_customer',
            field=models.CharField(default='none', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sell',
            name='to_customer',
            field=models.CharField(default='none', max_length=20),
            preserve_default=False,
        ),
    ]
