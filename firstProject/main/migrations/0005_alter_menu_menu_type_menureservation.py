# Generated by Django 4.0.6 on 2022-07-15 07:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0004_menu_menu_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='menu_type',
            field=models.CharField(choices=[('starters', 'Starters'), ('lunch', 'Lunch'), ('dinner', 'Dinner'), ('breakfast', 'Breakfast')], max_length=20, null=True),
        ),
        migrations.CreateModel(
            name='MenuReservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCurrent', models.DateTimeField(auto_now_add=True)),
                ('date', models.IntegerField()),
                ('time', models.IntegerField()),
                ('client_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('menu_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.menu')),
            ],
        ),
    ]
