# Generated by Django 3.1.5 on 2021-05-13 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_auto_20210512_1856'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='restaurant',
        ),
        migrations.AlterField(
            model_name='food',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name='Restaurant',
        ),
    ]