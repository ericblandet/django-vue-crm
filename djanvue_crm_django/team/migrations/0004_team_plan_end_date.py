# Generated by Django 4.1.7 on 2023-03-12 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0003_team_plan_status_team_stripe_customer_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='plan_end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
