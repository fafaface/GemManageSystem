# Generated by Django 3.1.3 on 2020-11-29 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gem_Manage_App', '0015_singlesample_is_select'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singlesample',
            name='is_select',
            field=models.CharField(choices=[(1, '无'), (2, '通过'), (3, '未通过')], default=1, max_length=10),
        ),
    ]