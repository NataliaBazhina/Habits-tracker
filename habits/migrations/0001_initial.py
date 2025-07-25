# Generated by Django 5.2.4 on 2025-07-21 14:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Habit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "place",
                    models.CharField(
                        help_text="укажите место, в котором необходимо выполнять привычку",
                        max_length=255,
                        verbose_name="место",
                    ),
                ),
                (
                    "time",
                    models.TimeField(
                        help_text="укажите время, когда необходимо выполнять привычку",
                        verbose_name="время",
                    ),
                ),
                (
                    "action",
                    models.CharField(
                        help_text="укажите действие, которое требуется выполнять",
                        max_length=255,
                        verbose_name="действие",
                    ),
                ),
                (
                    "nice_habit",
                    models.BooleanField(
                        default=False, verbose_name="приятная привычка"
                    ),
                ),
                (
                    "reward",
                    models.CharField(
                        blank=True,
                        help_text="укажите вознаграждение за выполнение привычки",
                        max_length=255,
                        null=True,
                        verbose_name="вознаграждение",
                    ),
                ),
                (
                    "periodicity",
                    models.PositiveSmallIntegerField(
                        default=1,
                        help_text="укажите периодичность выполнения привычки(например, 1 раз в день",
                        verbose_name="периодичность выполнения привычки",
                    ),
                ),
                (
                    "execution_time",
                    models.PositiveSmallIntegerField(
                        help_text="укажите сколько времени(в секундах) потребуется на выполнение привычки",
                        verbose_name="время в секундах",
                    ),
                ),
                (
                    "public_habit",
                    models.BooleanField(
                        default=False, verbose_name="признак публичности"
                    ),
                ),
                (
                    "related_habit",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="habits.habit",
                        verbose_name="связанная привычка",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        help_text="укажите создателя привычки",
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="создатель привычки",
                    ),
                ),
            ],
            options={
                "verbose_name": "Привычка",
                "verbose_name_plural": "Привычки",
            },
        ),
    ]
