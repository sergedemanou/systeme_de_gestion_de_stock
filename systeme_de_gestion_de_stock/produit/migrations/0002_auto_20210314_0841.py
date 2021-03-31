# Generated by Django 3.1.7 on 2021-03-14 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=300, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='produit',
            name='tag',
            field=models.ManyToManyField(to='produit.Tag'),
        ),
    ]