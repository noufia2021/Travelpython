# Generated by Django 4.2.7 on 2023-12-09 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inhome', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namet', models.CharField(max_length=250)),
                ('imgt', models.ImageField(upload_to='pics')),
                ('desct', models.TextField()),
            ],
        ),
    ]