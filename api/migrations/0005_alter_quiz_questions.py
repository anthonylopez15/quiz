# Generated by Django 3.2.7 on 2021-09-25 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_question_quiz_questions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='questions',
            field=models.ManyToManyField(to='api.Question'),
        ),
    ]
