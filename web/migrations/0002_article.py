# Generated by Django 3.0.4 on 2020-05-03 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('topic', models.ManyToManyField(related_name='topics', to='web.Topic')),
            ],
        ),
    ]
