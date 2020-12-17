# Generated by Django 3.1.3 on 2020-11-27 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Gem_Manage_App', '0012_auto_20201127_1108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sample',
            name='require',
        ),
        migrations.RemoveField(
            model_name='sample',
            name='sampletype',
        ),
        migrations.RemoveField(
            model_name='sample',
            name='status',
        ),
        migrations.AddField(
            model_name='singlesample',
            name='require',
            field=models.CharField(blank=True, max_length=50, verbose_name='检测要求'),
        ),
        migrations.AddField(
            model_name='singlesample',
            name='sample_type',
            field=models.CharField(choices=[(1, '大卡'), (2, '玉石'), (3, '钻石'), (4, '宝石'), (5, '小卡'), (6, '大报告')], default=1, max_length=10),
        ),
        migrations.AddField(
            model_name='singlesample',
            name='status',
            field=models.CharField(blank=True, max_length=50, verbose_name='样品状况'),
        ),
        migrations.AlterField(
            model_name='preinstall',
            name='sample_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gem_Manage_App.singlesample'),
        ),
        migrations.AlterField(
            model_name='singlesample',
            name='verification_code',
            field=models.CharField(max_length=10, null=True, verbose_name='验证码'),
        ),
        migrations.AlterField(
            model_name='task',
            name='identification_staff',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Gem_Manage_App.user'),
        ),
        migrations.AlterField(
            model_name='task',
            name='identification_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gem_Manage_App.sample'),
        ),
        migrations.AlterField(
            model_name='usergroupstatus',
            name='usergroup_status_values',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gem_Manage_App.sample'),
        ),
        migrations.DeleteModel(
            name='SampleType',
        ),
    ]
