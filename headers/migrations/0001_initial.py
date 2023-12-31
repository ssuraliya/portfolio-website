# Generated by Django 4.2 on 2023-11-12 17:12

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0089_log_entry_data_json_null_to_object'),
    ]

    operations = [
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Header for the site',
            },
            bases=(wagtail.models.PreviewableMixin, models.Model),
        ),
        migrations.CreateModel(
            name='HeaderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('link_title', models.CharField(blank=True, max_length=50, null=True)),
                ('link_url', models.CharField(blank=True, max_length=500)),
                ('open_in_new_tab', models.BooleanField(blank=True, default=False)),
                ('block_id', models.CharField(blank=True, help_text='ID of internal blocks of page.', max_length=255, null=True)),
                ('header', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='header_items', to='headers.header')),
                ('link_page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.page')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
