# Generated by Django 3.2 on 2021-05-31 03:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('entity', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Epic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('participating_heroes', models.ManyToManyField(to='entity.Hero')),
                ('participating_villains', models.ManyToManyField(to='entity.Villain')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.TextField()),
                ('years_ago', models.PositiveIntegerField()),
                ('epic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.epic')),
            ],
        ),
        migrations.CreateModel(
            name='EventVillain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_primary', models.BooleanField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.event')),
                ('hero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entity.villain')),
            ],
        ),
        migrations.CreateModel(
            name='EventHero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_primary', models.BooleanField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.event')),
                ('hero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entity.hero')),
            ],
        ),
    ]
