# Generated by Django 3.2.7 on 2021-09-25 06:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_auto_20210915_1939'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked_article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_liked', to='blog.article')),
                ('liked_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked_by_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
