# Generated by Django 2.2 on 2019-05-02 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oidc_provider', '0027_auto_20181003_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='code',
            name='rid',
            field=models.SmallIntegerField(null=True, verbose_name='RID'),
        ),
        migrations.AddField(
            model_name='token',
            name='rid',
            field=models.SmallIntegerField(null=True, verbose_name='RID'),
        ),
        migrations.AddField(
            model_name='userconsent',
            name='rid',
            field=models.SmallIntegerField(null=True, verbose_name='RID'),
        ),
    ]
