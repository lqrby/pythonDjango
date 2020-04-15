# Generated by Django 3.1 on 2020-03-25 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='名字', max_length=16)),
                ('gender', models.CharField(help_text='性别', max_length=8)),
                ('age', models.IntegerField()),
                ('moblie', models.IntegerField()),
                ('password', models.CharField(max_length=24)),
                ('email', models.CharField(help_text='电子邮件', max_length=8)),
                ('address', models.CharField(help_text='地址', max_length=8)),
            ],
        ),
    ]