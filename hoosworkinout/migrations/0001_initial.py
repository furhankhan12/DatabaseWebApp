# Generated by Django 3.0.5 on 2020-04-25 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('eid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=16)),
                ('comment', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'exercise',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('lid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=16)),
                ('address', models.CharField(max_length=50)),
                ('phone', models.CharField(blank=True, max_length=16, null=True)),
            ],
            options={
                'db_table': 'location',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=16)),
                ('middle_name', models.CharField(blank=True, max_length=16, null=True)),
                ('last_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=16)),
                ('email', models.CharField(max_length=16)),
                ('birthday', models.DateField()),
                ('body_weight', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('best_lift', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'user',
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
                ('username', models.ForeignKey(db_column='username', on_delete=django.db.models.deletion.CASCADE, to='hoosworkinout.User')),
            ],
            options={
                'db_table': 'workout',
            },
        ),
        migrations.CreateModel(
            name='WorkedOutAt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lid', models.ForeignKey(db_column='lid', on_delete=django.db.models.deletion.CASCADE, to='hoosworkinout.Location')),
                ('username', models.ForeignKey(db_column='username', on_delete=django.db.models.deletion.CASCADE, to='hoosworkinout.User')),
                ('wid', models.ForeignKey(db_column='wid', on_delete=django.db.models.deletion.CASCADE, to='hoosworkinout.Workout')),
            ],
            options={
                'db_table': 'worked_out_at',
            },
        ),
        migrations.CreateModel(
            name='Reps',
            fields=[
                ('numbers', models.IntegerField()),
                ('eid', models.ForeignKey(db_column='eid', on_delete=django.db.models.deletion.CASCADE, to='hoosworkinout.Exercise')),
            ],
            options={
                'db_table': 'reps',
            },
        ),
        migrations.AddField(
            model_name='exercise',
            name='username',
            field=models.ForeignKey(db_column='username', on_delete=django.db.models.deletion.CASCADE, to='hoosworkinout.User'),
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
                ('name', models.CharField(max_length=16)),
                ('description', models.CharField(max_length=100)),
                ('username', models.ForeignKey(db_column='username', on_delete=django.db.models.deletion.CASCADE, to='hoosworkinout.User')),
                ('wid', models.ForeignKey(db_column='wid', on_delete=django.db.models.deletion.CASCADE, to='hoosworkinout.Workout')),
            ],
            options={
                'db_table': 'plan',
                'unique_together': {('pid', 'wid')},
            },
        ),
    ]
