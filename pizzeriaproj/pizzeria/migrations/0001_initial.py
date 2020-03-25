# Generated by Django 3.0.4 on 2020-03-25 21:13

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
            name='PizzaType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typename', models.CharField(max_length=255)),
                ('typedescription', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name_plural': 'pizzatypes',
                'db_table': 'pizzatype',
            },
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizzaname', models.CharField(max_length=255)),
                ('pizzaprice', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('pizzaentrydate', models.DateField()),
                ('pizzaurl', models.URLField(blank=True, null=True)),
                ('pizzadescription', models.TextField()),
                ('pizzaimage', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('pizzatype', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pizzeria.PizzaType')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'pizzas',
                'db_table': 'pizza',
            },
        ),
    ]