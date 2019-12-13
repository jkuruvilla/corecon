# Generated by Django 3.0 on 2019-12-11 09:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('constraints', '0005_auto_20191205_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='entries_ion_frac',
            name='red_list',
            field=models.ManyToManyField(related_name='_entries_ion_frac_red_list_+', to='constraints.Entries_ion_frac'),
        ),
        migrations.AddField(
            model_name='entries_ion_frac',
            name='redshift_exp',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
