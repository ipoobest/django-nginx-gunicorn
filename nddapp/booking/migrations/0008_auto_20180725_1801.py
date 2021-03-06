# Generated by Django 2.0.7 on 2018-07-25 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_auto_20180724_1508'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='bw_to',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='bw_tr',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='fw_fm',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='fw_tr',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='loading',
        ),
        migrations.AddField(
            model_name='booking',
            name='backward_tr',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='booking',
            name='factory',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='booking',
            name='forward_tr',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='booking',
            name='pickup_form',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='booking',
            name='pickup_tr',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='booking',
            name='return_to',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='booking',
            name='return_tr',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
    ]
