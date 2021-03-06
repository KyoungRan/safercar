# Generated by Django 2.0 on 2018-02-03 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('desucar', '0010_car_simple_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='revision',
            name='car',
        ),
        migrations.RemoveField(
            model_name='defect',
            name='target',
        ),
        migrations.AddField(
            model_name='defect',
            name='car',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='desucar.Car'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='defect',
            name='fix_end',
            field=models.DateField(default='9999-12-31'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='defect',
            name='fix_start',
            field=models.DateField(default='9999-12-13'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='defect',
            name='kind',
            field=models.CharField(choices=[('RC', '리콜'), ('FF', '무상수리')], default='', max_length=2),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Revision',
        ),
    ]
