# Generated by Django 4.2 on 2024-05-05 11:45

from django.db import migrations, models
import nxtbn.core.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, nxtbn.core.models.SEOMixin),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('is_live', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=200)),
                ('content', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, nxtbn.core.models.SEOMixin),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]