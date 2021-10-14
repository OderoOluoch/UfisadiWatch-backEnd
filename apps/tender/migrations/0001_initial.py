# Generated by Django 3.2.8 on 2021-10-14 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tender_no', models.CharField(error_messages={'max_length': 'The tender NO exceeds max_lenght.'}, max_length=200, verbose_name='tender number')),
                ('description', models.TextField(blank=True, error_messages={'max_length': 'The description is too long. Use a maximum of 2000 characters.'}, max_length=2000, null=True, verbose_name='description')),
                ('entity_name', models.CharField(error_messages={'max_length': 'The entity name is too long. Use a maximum of 100 characters.'}, max_length=100, verbose_name='entity')),
                ('procurement_method', models.CharField(blank=True, choices=[('Expression of Interest', 'Expression of Interest'), ('Open Tender', 'Open Tender'), ('Restricted Tendering', 'Restricted Tendering')], error_messages={'max_length': 'The hint is too long. Use a maximum of 200 characters.'}, max_length=200, null=True, verbose_name='procurement method')),
                ('procurement_category', models.CharField(blank=True, choices=[('Consultancy Services', 'Consultancy Services'), ('Goods', 'Goods'), ('Works', 'Works'), ('Non Consultancy Services', 'Non Consultancy Services')], error_messages={'max_length': 'The hint is too long. Use a maximum of 150 characters.'}, max_length=150, null=True, verbose_name='procurement category')),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_rejected', models.BooleanField(default=False)),
                ('is_published', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('submitted_at', models.DateTimeField(blank=True, null=True)),
                ('closing_date', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to='core.user')),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.user')),
                ('evaluated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='evaluated_by', to='core.user')),
                ('last_updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='last_updated_by', to='core.user')),
                ('submitted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='submitted_by', to='core.user')),
            ],
        ),
    ]
