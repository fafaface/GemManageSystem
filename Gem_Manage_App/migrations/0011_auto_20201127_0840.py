# Generated by Django 3.1.3 on 2020-11-27 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gem_Manage_App', '0010_auto_20201127_0106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='payment_state',
            field=models.CharField(choices=[('是', '是'), ('否', '否')], default='non_active', max_length=10, verbose_name='是否付款'),
        ),
    ]
