# Generated by Django 5.1.1 on 2024-10-07 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_rename_payment_day_payment_payment_date"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="payment",
            options={
                "ordering": ("payment_date",),
                "verbose_name": "Платеж",
                "verbose_name_plural": "Платежи",
            },
        ),
    ]