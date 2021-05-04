# Generated by Django 3.2 on 2021-05-04 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20210503_0953'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Supplers',
            new_name='Suppliers',
        ),
        migrations.AddField(
            model_name='company',
            name='facility_type',
            field=models.CharField(choices=[('Depot', 'Depot'), ('Truck', 'Truck'), ('Service', 'Service'), ('Filling Station', 'Filling Station')], default=0, max_length=50),
            preserve_default=False,
        ),
    ]
