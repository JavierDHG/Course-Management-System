# Generated by Django 5.1.7 on 2025-05-27 16:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pages', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='my_course_list',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_course_list', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='status_pay',
            name='pay_package_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status_pay', to='pages.pay_package'),
        ),
        migrations.AddField(
            model_name='status_pay',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status_pay', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='my_course_list',
            unique_together={('user', 'course')},
        ),
    ]
