# Generated by Django 4.1.4 on 2023-05-31 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('corses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='themeslevelcourses',
            name='сorse',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='corses.corses', verbose_name='Курс'),
            preserve_default=False,
        ),
    ]
