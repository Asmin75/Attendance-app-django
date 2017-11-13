# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-11-03 05:03
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='student_teacher',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='teacher_class',
        ),
        migrations.AddField(
            model_name='school',
            name='school_classes',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Pre-Nursery', 'Pre-Nursery'), ('Nursery', 'Pre-Nursery'), ('Kindergarten', 'Kindergarten'), ('I', 'I'), ('II', 'II'), ('III', 'III'), ('IV', 'IV'), ('V', 'V'), ('VI', 'VI'), ('VII', 'VII'), ('VIII', 'VIII'), ('IX', 'IX'), ('X', 'X'), ('XI', 'XI'), ('XII', 'XII')], default=1, max_length=70),
        ),
    ]