# Generated by Django 3.2.6 on 2021-08-31 04:42

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='description',
            field=ckeditor.fields.RichTextField(default='hey it is null'),
            preserve_default=False,
        ),
    ]
