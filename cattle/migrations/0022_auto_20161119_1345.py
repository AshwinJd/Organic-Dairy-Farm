# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-19 08:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cattle', '0021_auto_20161119_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calf',
            name='Insurance',
            field=models.BooleanField(choices=[(b'Yes', b'Yes'), (b'No', b'No')], default=b'No'),
        ),
        migrations.AlterField(
            model_name='calf',
            name='One_time_Vaccination',
            field=models.BooleanField(choices=[(b'Yes', b'Yes'), (b'No', b'No')], default=b'No'),
        ),
        migrations.AlterField(
            model_name='calf',
            name='dehorning',
            field=models.BooleanField(choices=[(b'Yes', b'Yes'), (b'No', b'No')], default=b'No'),
        ),
        migrations.AlterField(
            model_name='cattle',
            name='Confirmation_after_oneMonth',
            field=models.BooleanField(choices=[(b'Yes', b'Yes'), (b'No', b'No')], default=b'No'),
        ),
        migrations.AlterField(
            model_name='cattle',
            name='Confirmation_after_threeMonth',
            field=models.BooleanField(choices=[(b'Yes', b'Yes'), (b'No', b'No')], default=b'No'),
        ),
        migrations.AlterField(
            model_name='cattle',
            name='Deworming_1st_quarter_confirmation',
            field=models.BooleanField(choices=[(b'Yes', b'Yes'), (b'No', b'No')], default=b'No'),
        ),
        migrations.AlterField(
            model_name='cattle',
            name='Deworming_2nd_quarter_confirmation',
            field=models.BooleanField(choices=[(b'Yes', b'Yes'), (b'No', b'No')], default=b'No'),
        ),
        migrations.AlterField(
            model_name='cattle',
            name='Deworming_3rd_quarter_confirmation',
            field=models.BooleanField(choices=[(b'Yes', b'Yes'), (b'No', b'No')], default=b'No'),
        ),
        migrations.AlterField(
            model_name='cattle',
            name='Deworming_4th_quarter_confirmation',
            field=models.BooleanField(choices=[(b'Yes', b'Yes'), (b'No', b'No')], default=b'No'),
        ),
        migrations.AlterField(
            model_name='cattle',
            name='Insurance',
            field=models.BooleanField(choices=[(b'Yes', b'Yes'), (b'No', b'No')], default=b'No'),
        ),
        migrations.AlterField(
            model_name='cattle',
            name='Vaccine_BQ_confirmation',
            field=models.BooleanField(choices=[(b'Yes', b'Yes'), (b'No', b'No')], default=b'No'),
        ),
        migrations.AlterField(
            model_name='cattle',
            name='Vaccine_FMD_confirmation',
            field=models.BooleanField(choices=[(b'Yes', b'Yes'), (b'No', b'No')], default=b'No'),
        ),
        migrations.AlterField(
            model_name='cattle',
            name='Vaccine_HS_confirmation',
            field=models.BooleanField(choices=[(b'Yes', b'Yes'), (b'No', b'No')], default=b'No'),
        ),
        migrations.AlterField(
            model_name='cattle',
            name='Vaccine_for_Brucella_confirmation',
            field=models.BooleanField(choices=[(b'Yes', b'Yes'), (b'No', b'No')], default=b'No'),
        ),
        migrations.AlterField(
            model_name='cattle',
            name='Vaccine_for_Theileriosis_confirmation',
            field=models.BooleanField(choices=[(b'Yes', b'Yes'), (b'No', b'No')], default=b'No'),
        ),
        migrations.AlterField(
            model_name='cattle',
            name='dehorning',
            field=models.BooleanField(choices=[(b'Yes', b'Yes'), (b'No', b'No')], default=b'No'),
        ),
    ]
