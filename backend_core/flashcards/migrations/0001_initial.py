# Generated by Django 4.1.7 on 2023-03-13 22:29

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
            name='Deck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=32, null=True)),
                ('rating', models.IntegerField(blank=True, default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DifficultyLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('value', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24)),
            ],
        ),
        migrations.CreateModel(
            name='FlashCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=32, null=True)),
                ('rating', models.IntegerField(blank=True, default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s', to=settings.AUTH_USER_MODEL)),
                ('deck', models.ManyToManyField(related_name='flashcards', to='flashcards.deck')),
                ('difficulty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s', to='flashcards.difficultylevel')),
                ('tags', models.ManyToManyField(related_name='%(class)s', to='flashcards.tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='deck',
            name='difficulty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s', to='flashcards.difficultylevel'),
        ),
        migrations.AddField(
            model_name='deck',
            name='tags',
            field=models.ManyToManyField(related_name='%(class)s', to='flashcards.tag'),
        ),
    ]
