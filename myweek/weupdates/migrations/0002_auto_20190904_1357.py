# Generated by Django 2.2.5 on 2019-09-04 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weupdates', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='action',
            name='goodbad',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='action',
            name='choice',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='weupdates.Choice'),
        ),
    ]
