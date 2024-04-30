# Generated by Django 4.2 on 2024-04-30 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_status',
            field=models.CharField(choices=[('AUTHORIZED', 'Authorized'), ('CAPTURED', 'Captured'), ('FAILED', 'Failed'), ('REFUNDED', 'Refunded'), ('CANCELED', 'Canceled')], default='AUTHORIZED', max_length=20),
        ),
    ]
