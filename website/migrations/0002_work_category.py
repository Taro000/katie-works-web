# Generated by Django 3.2.4 on 2021-07-10 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='category',
            field=models.CharField(choices=[('LG', 'Logo'), ('CL', 'Catalogue'), ('AD', 'Advertisement'), ('OT', 'Others')], default='OT', max_length=2, verbose_name='カテゴリー'),
            preserve_default=False,
        ),
    ]
