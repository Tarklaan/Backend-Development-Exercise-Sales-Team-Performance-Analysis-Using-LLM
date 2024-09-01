# Generated by Django 5.0.3 on 2024-09-01 00:21

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SalesData",
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
                ("employee_id", models.IntegerField()),
                ("employee_name", models.CharField(max_length=255)),
                ("created", models.CharField(max_length=255)),
                ("dated", models.DateField()),
                ("lead_taken", models.IntegerField()),
                ("tours_booked", models.IntegerField()),
                ("applications", models.IntegerField()),
                ("tours_per_lead", models.FloatField()),
                ("apps_per_tour", models.FloatField()),
                ("apps_per_lead", models.FloatField()),
                ("revenue_confirmed", models.FloatField()),
                ("revenue_pending", models.FloatField()),
                ("revenue_runrate", models.FloatField()),
                ("tours_in_pipeline", models.IntegerField()),
                ("avg_deal_value_30_days", models.FloatField()),
                ("avg_close_rate_30_days", models.FloatField()),
                ("estimated_revenue", models.FloatField()),
                ("tours", models.IntegerField()),
                ("tours_runrate", models.FloatField()),
                ("tours_scheduled", models.IntegerField()),
                ("tours_pending", models.IntegerField()),
                ("tours_cancelled", models.IntegerField()),
                ("mon_text", models.TextField()),
                ("tue_text", models.TextField()),
                ("wed_text", models.TextField()),
                ("thur_text", models.TextField()),
                ("fri_text", models.TextField()),
                ("sat_text", models.TextField()),
                ("sun_text", models.TextField()),
                ("mon_call", models.IntegerField()),
                ("tue_call", models.IntegerField()),
                ("wed_call", models.IntegerField()),
                ("thur_call", models.IntegerField()),
                ("fri_call", models.IntegerField()),
                ("sat_call", models.IntegerField()),
                ("sun_call", models.IntegerField()),
            ],
        ),
    ]
