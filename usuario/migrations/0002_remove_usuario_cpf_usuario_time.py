# Generated by Django 4.2.6 on 2023-11-06 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("bolanarede", "0002_delete_teste"),
        ("usuario", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="usuario",
            name="cpf",
        ),
        migrations.AddField(
            model_name="usuario",
            name="time",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="usuarios",
                to="bolanarede.time",
            ),
        ),
    ]
