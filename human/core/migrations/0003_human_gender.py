# Generated by Django 3.2.3 on 2021-05-23 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_human_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='human',
            name='gender',
            field=models.ForeignKey(blank=True, help_text='Пол.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='humans_gender', related_query_name='human_gender', to='core.gender', verbose_name='Gender:'),
        ),
    ]
