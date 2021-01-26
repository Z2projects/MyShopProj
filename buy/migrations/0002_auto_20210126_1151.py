# Generated by Django 3.1.5 on 2021-01-26 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ptype', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='buy',
            old_name='quantity',
            new_name='bquantity',
        ),
        migrations.RenameField(
            model_name='buy',
            old_name='rate',
            new_name='brate',
        ),
        migrations.RemoveField(
            model_name='buy',
            name='name',
        ),
        migrations.RemoveField(
            model_name='buy',
            name='ptype',
        ),
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sdate', models.DateField()),
                ('srate', models.IntegerField()),
                ('squantity', models.IntegerField()),
                ('sp', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='buy.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='ptype',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='buy.producttype'),
        ),
        migrations.AddField(
            model_name='buy',
            name='bp',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='buy.product'),
        ),
    ]
