# Generated by Django 3.1.1 on 2021-01-15 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20210115_1433'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='portfolio',
        ),
        migrations.AddField(
            model_name='education',
            name='portfolio',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='portfolio_Education', to='portfolio.portfolio'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='experience',
            name='portfolio',
        ),
        migrations.AddField(
            model_name='experience',
            name='portfolio',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='portfolio_Ecperiece', to='portfolio.portfolio'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='project',
            name='portfolio',
        ),
        migrations.AddField(
            model_name='project',
            name='portfolio',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='portfolio_Project', to='portfolio.portfolio'),
            preserve_default=False,
        ),
    ]