# Generated by Django 5.0.6 on 2024-07-26 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player1_id', models.IntegerField()),
                ('player2_id', models.IntegerField()),
                ('player1_nick', models.CharField(default='bontarien')),
                ('player2_nick', models.CharField(default='brakmarien')),
                ('player1_score', models.IntegerField()),
                ('player2_score', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]