# Generated by Django 4.2 on 2023-11-12 17:50

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='blocks',
            field=wagtail.fields.StreamField([('name_section', wagtail.blocks.StructBlock([('id', wagtail.blocks.CharBlock(help_text='ID of this block. Can be used to link the block in header', null=True, required=False)), ('name', wagtail.blocks.CharBlock(required=True)), ('position', wagtail.blocks.CharBlock(required=True)), ('company_name', wagtail.blocks.CharBlock(required=True))]))], blank=True, use_json_field=True, verbose_name='Page body'),
        ),
    ]