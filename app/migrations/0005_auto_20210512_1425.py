# Generated by Django 3.1.7 on 2021-05-12 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210512_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspectionchecklist',
            name='remarks',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='inspectionchecklist',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
