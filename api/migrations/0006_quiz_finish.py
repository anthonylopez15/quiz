# Generated by Django 3.2.7 on 2021-09-27 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_quiz_questions'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='finish',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
