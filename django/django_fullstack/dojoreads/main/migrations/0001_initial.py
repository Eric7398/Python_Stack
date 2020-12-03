# Generated by Django 2.2.4 on 2020-11-12 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_reg_app', '0005_auto_20201112_1054'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=255)),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('byuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='byusers', to='login_reg_app.User')),
                ('forbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='forbooks', to='main.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ManyToManyField(related_name='authors', to='main.Book')),
            ],
        ),
    ]