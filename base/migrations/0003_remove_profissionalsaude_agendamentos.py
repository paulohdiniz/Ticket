# Generated by Django 5.0.3 on 2024-04-12 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0002_remove_customer_agendamentos"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profissionalsaude",
            name="agendamentos",
        ),
    ]
