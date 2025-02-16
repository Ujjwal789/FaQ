# Generated by Django 5.1.5 on 2025-02-01 13:48

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faqs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faq',
            name='answer_bn',
        ),
        migrations.RemoveField(
            model_name='faq',
            name='answer_hi',
        ),
        migrations.RemoveField(
            model_name='faq',
            name='question_bn',
        ),
        migrations.RemoveField(
            model_name='faq',
            name='question_hi',
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question',
            field=models.CharField(max_length=255),
        ),
    ]
