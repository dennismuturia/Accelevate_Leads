
from django.db import migrations


def create_subjects(apps, schema_editor):
    Subject = apps.get_model('classroom', 'Subject')
    Subject.objects.create(name='Jomo Kenyatta University of Technology', color='#343a40')
    Subject.objects.create(name='The University of Nairobi', color='#007bff')
    Subject.objects.create(name='Kenyatta University', color='#28a745')
    Subject.objects.create(name='Technical university of Kenya', color='#17a2b8')
    Subject.objects.create(name='Riara University', color='#ffc107')


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_subjects),
]