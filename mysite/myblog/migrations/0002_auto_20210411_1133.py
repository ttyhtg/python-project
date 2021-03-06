# Generated by Django 2.0 on 2021-04-11 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=191)),
                ('email', models.EmailField(max_length=254)),
                ('update_time', models.DateTimeField(auto_now=True, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('null_test', models.CharField(max_length=200, null=True)),
                ('blank_test', models.CharField(max_length=200, null=True)),
                ('whether_vip', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
