# Generated by Django 3.1.3 on 2020-12-03 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gem_Manage_App', '0022_auto_20201129_2253'),
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('member_name', models.CharField(max_length=50)),
                ('telephone', models.CharField(max_length=50)),
                ('member_type', models.CharField(max_length=50)),
                ('legal_representative', models.CharField(max_length=50)),
                ('license_number', models.CharField(max_length=50)),
                ('postal_code', models.CharField(max_length=50)),
                ('company_name', models.CharField(max_length=100)),
                ('company_address', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Member',
        ),
    ]
