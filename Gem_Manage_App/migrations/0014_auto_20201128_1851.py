# Generated by Django 3.1.3 on 2020-11-28 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gem_Manage_App', '0013_auto_20201127_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singlesample',
            name='image',
            field=models.FileField(null=True, upload_to='', verbose_name='图片'),
        ),
    ]