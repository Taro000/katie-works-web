# Generated by Django 3.2.4 on 2021-07-15 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_work_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='thumbnail',
            field=models.ImageField(max_length=32, upload_to='work', verbose_name='サムネイル'),
        ),
    ]