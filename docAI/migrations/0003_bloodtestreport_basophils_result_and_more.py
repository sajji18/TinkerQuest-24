# Generated by Django 5.0.3 on 2024-03-18 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docAI', '0002_remove_message_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloodtestreport',
            name='Basophils_result',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bloodtestreport',
            name='Eosinophils_result',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bloodtestreport',
            name='Lymphocytes_result',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bloodtestreport',
            name='Monocytes_result',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bloodtestreport',
            name='Neutrophils_result',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bloodtestreport',
            name='PCV_result',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bloodtestreport',
            name='Platelet_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bloodtestreport',
            name='RBC_result',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bloodtestreport',
            name='WBC_result',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bloodtestreport',
            name='hemoglobin_result',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=4),
            preserve_default=False,
        ),
    ]