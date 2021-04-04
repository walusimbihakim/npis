# Generated by Django 3.1.7 on 2021-04-04 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210404_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='sample',
            name='parameter',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sample',
            name='sample_request',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='app.samplerequest'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sample',
            name='test_method',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sample',
            name='type_method',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sample',
            name='unit_fee',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='samplerequest',
            name='reg_no',
            field=models.CharField(max_length=50, unique=True, verbose_name='Request No.'),
        ),
    ]
