from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cv", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="taidot",
            old_name="taido",
            new_name="taito",
        ),
    ]

