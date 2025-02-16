# Generated by Django 5.1.5 on 2025-02-03 10:36

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faqs', '0002_remove_faq_answer_bn_remove_faq_answer_hi_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='answer_bn',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Answer in Bengali'),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_hi',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Answer in Hindi'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_bn',
            field=models.TextField(blank=True, null=True, verbose_name='Question in Bengali'),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_hi',
            field=models.TextField(blank=True, null=True, verbose_name='Question in Hindi'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=ckeditor.fields.RichTextField(verbose_name='Answer'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question',
            field=models.TextField(verbose_name='Question'),
        ),
    ]
