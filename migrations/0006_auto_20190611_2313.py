# Generated by Django 2.2.2 on 2019-06-11 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taswira', '0005_auto_20190611_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post1',
            name='cvs_path',
            field=models.FileField(upload_to='static/taswira/dataset'),
        ),
    ]
