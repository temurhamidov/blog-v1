# Generated by Django 4.1.6 on 2023-02-06 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_blog_slug_alter_category_slug_alter_tag_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name': 'Blog', 'verbose_name_plural': 'Bloglar'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Kategoriya', 'verbose_name_plural': 'Kategoriyalar'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Tag', 'verbose_name_plural': 'Taglar'},
        ),
    ]
