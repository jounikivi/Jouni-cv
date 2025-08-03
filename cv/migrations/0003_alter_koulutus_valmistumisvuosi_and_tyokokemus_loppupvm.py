from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0002_rename_taido_to_taito'),
    ]

    operations = [
        migrations.AlterField(
            model_name='koulutus',
            name='valmistumisvuosi',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tyokokemus',
            name='loppupvm',
            field=models.DateField(blank=True, null=True),
        ),
    ]
