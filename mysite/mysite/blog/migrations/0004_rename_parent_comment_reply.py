# Generated by Django 3.2.6 on 2021-08-20 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment_parent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='parent',
            new_name='reply',
        ),
    ]
