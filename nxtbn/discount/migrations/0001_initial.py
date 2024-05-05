# Generated by Django 4.2 on 2024-05-05 11:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PromoCode',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(max_length=20, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('code_type', models.CharField(choices=[('PERCENTAGE', 'Percentage'), ('FIXED', 'Fixed Amount')], default='PERCENTAGE', max_length=20)),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('expiration_date', models.DateTimeField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
