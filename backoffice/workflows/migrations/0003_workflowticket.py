# Generated by Django 4.2.6 on 2023-11-20 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("workflows", "0002_workflow_remove_workflowmeta_id_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="WorkflowTicket",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("ticket_id", models.CharField(max_length=32)),
                (
                    "workflow_id",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="workflows.workflow"),
                ),
            ],
        ),
    ]