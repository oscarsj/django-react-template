# Generated by Django 3.1.2 on 2020-10-24 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('children', '0004_auto_20201024_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registeredchild',
            name='child',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='children.child'),
        ),
        migrations.AlterField(
            model_name='registeredchild',
            name='season',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='children.season'),
        ),
    ]