# Generated by Django 2.2.3 on 2019-08-02 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mackta_api', '0005_delete_profilefeeditem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crawling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]