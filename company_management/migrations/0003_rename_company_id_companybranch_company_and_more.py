# Generated by Django 4.2.1 on 2023-05-15 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_management', '0002_remove_companybranch_status_company_created_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companybranch',
            old_name='company_id',
            new_name='company',
        ),
        migrations.AddField(
            model_name='companybranch',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
