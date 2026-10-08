from django.db import migrations


def create_categories(apps, schema_editor):
    Category = apps.get_model('jobs', 'Category')
    categories = [
        ('Software Development', 'Programming, engineering, and dev roles'),
        ('Design', 'UI/UX, graphic, and product design'),
        ('Marketing', 'Digital marketing, SEO, content, and growth'),
        ('Sales', 'Business development and sales roles'),
        ('Customer Support', 'Support, success, and service roles'),
        ('Data Science', 'Data analysis, ML, and analytics'),
        ('Human Resources', 'Recruiting, HR, and people operations'),
        ('Finance', 'Accounting, finance, and analyst roles'),
    ]

    for name, description in categories:
        Category.objects.get_or_create(name=name, defaults={'description': description})


def remove_categories(apps, schema_editor):
    Category = apps.get_model('jobs', 'Category')
    Category.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),  # adjust to your latest jobs migration if different
    ]

    operations = [
        migrations.RunPython(create_categories, remove_categories),
    ]