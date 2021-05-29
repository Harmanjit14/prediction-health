# Generated by Django 3.1.7 on 2021-05-29 23:32

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('carbs', models.FloatField(default=0)),
                ('proteins', models.FloatField(default=0)),
                ('fats', models.FloatField(default=0)),
                ('vitA', models.FloatField(default=0)),
                ('vitD', models.FloatField(default=0)),
                ('vitC', models.FloatField(default=0)),
                ('vitE', models.FloatField(default=0)),
                ('Sodium', models.FloatField(default=0)),
                ('Iron', models.FloatField(default=0)),
                ('Potassium', models.FloatField(default=0)),
                ('Calcium', models.FloatField(default=0)),
                ('Magnesium', models.FloatField(default=0)),
                ('Zinc', models.FloatField(default=0)),
                ('Phosphorus', models.FloatField(default=0)),
                ('omega3', models.FloatField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.userclass')),
            ],
        ),
    ]
