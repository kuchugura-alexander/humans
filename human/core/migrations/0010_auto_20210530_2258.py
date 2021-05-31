# Generated by Django 3.2.3 on 2021-05-30 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_token'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='token',
            options={'ordering': ('modified_at',), 'verbose_name': 'Токен', 'verbose_name_plural': 'Токены'},
        ),
        migrations.AddField(
            model_name='token',
            name='active',
            field=models.BooleanField(default=False, help_text='Активность.', verbose_name='Active:'),
        ),
        migrations.AlterField(
            model_name='token',
            name='token',
            field=models.CharField(blank=True, default='', help_text='Токен.', max_length=20, unique=True, verbose_name='Token:'),
        ),
    ]
