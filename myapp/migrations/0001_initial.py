# Generated by Django 5.1.7 on 2025-04-04 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Photo', models.ImageField(upload_to='myimage')),
                ('Date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
