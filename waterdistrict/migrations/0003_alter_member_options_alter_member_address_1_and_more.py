# Generated by Django 4.1.2 on 2022-10-04 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waterdistrict', '0002_auto_20190623_2031'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='member',
            options={'ordering': ['owner']},
        ),
        migrations.AlterField(
            model_name='member',
            name='address_1',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='member',
            name='address_2',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]