# Generated by Django 3.2.6 on 2021-08-20 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_rename_parent_comment_reply'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='reply',
            new_name='parent',
        ),
    ]
