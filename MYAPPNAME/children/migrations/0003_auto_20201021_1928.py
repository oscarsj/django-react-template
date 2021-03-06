# Generated by Django 3.1.2 on 2020-10-21 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('children', '0002_auto_20201021_1907'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='child',
            options={'ordering': ['first_surname', 'second_surname', 'name', 'birthdate']},
        ),
        migrations.AlterField(
            model_name='child',
            name='address',
            field=models.CharField(blank=True, default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='child',
            name='birthdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='child',
            name='dni',
            field=models.CharField(blank=True, default='', max_length=9),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='child',
            name='first_surname',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='child',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='child',
            name='notes',
            field=models.CharField(blank=True, default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='child',
            name='parents',
            field=models.ManyToManyField(blank=True, null=True, to='children.Parent'),
        ),
        migrations.AlterField(
            model_name='child',
            name='postcode',
            field=models.CharField(blank=True, default='', max_length=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='child',
            name='school',
            field=models.CharField(blank=True, default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='child',
            name='second_surname',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='child',
            name='telephone',
            field=models.CharField(blank=True, default='', max_length=13),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='child',
            name='telephone2',
            field=models.CharField(blank=True, default='', max_length=13),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='child',
            name='town',
            field=models.CharField(blank=True, default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='location',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='parent',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='parent',
            name='first_surname',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='parent',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='parent',
            name='second_surname',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='season',
            name='active',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='season',
            name='children',
            field=models.ManyToManyField(blank=True, null=True, through='children.RegisteredChild', to='children.Child'),
        ),
        migrations.AlterField(
            model_name='season',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='children.course'),
        ),
        migrations.AlterField(
            model_name='season',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='season',
            name='monitors',
            field=models.ManyToManyField(blank=True, to='children.Monitor'),
        ),
        migrations.AlterField(
            model_name='season',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='season',
            name='start_date',
            field=models.DateField(),
        ),
    ]
