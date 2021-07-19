# Generated by Django 3.2.5 on 2021-07-18 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("record_requests", "0003_auto_20210715_2300"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recordrequest",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="recordrequest",
            name="estimated_response_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="recordrequest",
            name="filed_at",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="recordrequest",
            name="last_communication_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="recordrequestfile",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="recordrequestfile",
            name="title",
            field=models.CharField(max_length=256, null=True),
        ),
    ]
