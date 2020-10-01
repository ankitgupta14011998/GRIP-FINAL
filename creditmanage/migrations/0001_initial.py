# Generated by Django 3.1.2 on 2020-10-01 06:27

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='people',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('credit', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Credit_Amount', models.IntegerField()),
                ('Date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Senderbalance', models.IntegerField()),
                ('Receiverbalance', models.IntegerField()),
                ('Receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='creditmanage.people')),
                ('Sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='creditmanage.people')),
            ],
        ),
    ]