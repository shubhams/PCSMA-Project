# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_userprofile_auth_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='day',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
    ]
