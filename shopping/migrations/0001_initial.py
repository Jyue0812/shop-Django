# Generated by Django 2.0.5 on 2018-07-06 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='category')),
                ('price', models.DecimalField(decimal_places=4, max_digits=10)),
                ('stock', models.BooleanField(default=0)),
                ('selling', models.BooleanField(default=True)),
                ('createdat', models.DateTimeField(auto_now_add=True)),
                ('updatedat', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Goods',
                'ordering': ('createdat',),
            },
        ),
        migrations.CreateModel(
            name='GoodsType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='category')),
            ],
            options={
                'db_table': 'GoodsType',
            },
        ),
        migrations.AddField(
            model_name='goods',
            name='goodstype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.GoodsType'),
        ),
    ]
