# Generated by Django 2.0.1 on 2018-01-22 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desucar', '0003_auto_20171223_1018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='revision',
            name='year',
        ),
        migrations.AddField(
            model_name='revision',
            name='production_end',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='revision',
            name='production_start',
            field=models.DateField(default='1970-01-01'),
            preserve_default=False,
        ),
    ]
