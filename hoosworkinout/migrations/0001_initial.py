# Generated by Django 3.0.5 on 2020-04-26 00:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('eid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=16)),
                ('comment', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.ForeignKey(db_column='username', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'exercise',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('lid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('phone', models.CharField(blank=True, max_length=16, null=True)),
            ],
            options={
                'db_table': 'location',
            },
        ),
        migrations.CreateModel(
            name='Cardio',
            fields=[
                ('eid', models.OneToOneField(db_column='eid', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='hoosworkinout.Exercise')),
                ('duration', models.IntegerField()),
                ('distance', models.DecimalField(decimal_places=1, max_digits=4)),
                ('calories_burned', models.IntegerField(blank=True, null=True)),
                ('peak_heartrate', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cardio',
            },
        ),
        migrations.CreateModel(
            name='Hiit',
            fields=[
                ('eid', models.OneToOneField(db_column='eid', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='hoosworkinout.Exercise')),
                ('distance', models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True)),
                ('name', models.CharField(max_length=16)),
                ('calories_burned', models.IntegerField()),
                ('peak_heartrate', models.IntegerField()),
                ('rest_interval', models.IntegerField()),
                ('work_interval', models.IntegerField()),
            ],
            options={
                'db_table': 'hiit',
            },
        ),
        migrations.CreateModel(
            name='Strength',
            fields=[
                ('eid', models.OneToOneField(db_column='eid', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='hoosworkinout.Exercise')),
                ('weight', models.IntegerField()),
                ('category', models.CharField(max_length=24)),
                ('sets', models.IntegerField()),
            ],
            options={
                'db_table': 'strength',
            },
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('wid', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('user', models.ForeignKey(db_column='username', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'workout',
            },
        ),
        migrations.CreateModel(
            name='WorkedOutAt',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('lid', models.ForeignKey(db_column='lid', on_delete=django.db.models.deletion.CASCADE, to='hoosworkinout.Location')),
                ('user', models.ForeignKey(db_column='username', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('wid', models.ForeignKey(db_column='wid', on_delete=django.db.models.deletion.CASCADE, to='hoosworkinout.Workout')),
            ],
            options={
                'db_table': 'worked_out_at',
            },
        ),
        migrations.CreateModel(
            name='Reps',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('numbers', models.IntegerField()),
                ('eid', models.ForeignKey(db_column='eid', on_delete=django.db.models.deletion.CASCADE, to='hoosworkinout.Exercise')),
            ],
            options={
                'db_table': 'reps',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday', models.DateField()),
                ('body_weight', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('best_lift', models.IntegerField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'profile',
            },
        ),
        migrations.AddField(
            model_name='exercise',
            name='wid',
            field=models.ForeignKey(db_column='wid', on_delete=django.db.models.deletion.CASCADE, to='hoosworkinout.Workout'),
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('user', models.ForeignKey(db_column='username', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('wid', models.ForeignKey(db_column='wid', on_delete=django.db.models.deletion.CASCADE, to='hoosworkinout.Workout')),
            ],
            options={
                'db_table': 'plan',
                'unique_together': {('pid', 'wid')},
            },
        ),
    ]
