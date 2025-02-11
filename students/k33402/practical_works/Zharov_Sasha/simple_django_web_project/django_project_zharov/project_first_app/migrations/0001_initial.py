# Generated by Django 4.2.6 on 2023-10-10 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=15, verbose_name='Гос номер')),
                ('brand', models.CharField(max_length=20, verbose_name='Марка')),
                ('car_model', models.CharField(max_length=20, verbose_name='Модель')),
                ('color', models.CharField(blank=True, max_length=30, null=True, verbose_name='Цвет')),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('birth_date', models.DateTimeField(null=True, verbose_name='Дата рождения')),
            ],
        ),
        migrations.CreateModel(
            name='Ownership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateField(verbose_name='Дата начала')),
                ('date_end', models.DateField(verbose_name='Дата окончания')),
                ('car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project_first_app.car')),
                ('driver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project_first_app.driver')),
            ],
        ),
        migrations.CreateModel(
            name='DriverLicence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10, verbose_name='Номер удостоверения')),
                ('type', models.CharField(max_length=10, verbose_name='Тип')),
                ('release_date', models.DateTimeField(verbose_name='Дата выдачи')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.driver')),
            ],
        ),
        migrations.AddField(
            model_name='driver',
            name='cars',
            field=models.ManyToManyField(through='project_first_app.Ownership', to='project_first_app.car'),
        ),
        migrations.AddField(
            model_name='car',
            name='drivers',
            field=models.ManyToManyField(through='project_first_app.Ownership', to='project_first_app.driver'),
        ),
    ]
