# Generated by Django 3.1.3 on 2020-11-26 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gem_Manage_App', '0009_auto_20201126_2323'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sender',
            old_name='sender_postalcode',
            new_name='postal_code',
        ),
        migrations.RenameField(
            model_name='sender',
            old_name='sender_name',
            new_name='sample_sender',
        ),
        migrations.RemoveField(
            model_name='receipts',
            name='sender',
        ),
        migrations.AddField(
            model_name='receipts',
            name='sample_sender',
            field=models.TextField(default='xxx'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sample',
            name='receipt_tel',
            field=models.CharField(default='111', max_length=20, verbose_name='检测室电话'),
            preserve_default=False,
        ),
    ]
