# Generated by Django 4.2.8 on 2024-01-26 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srcs_user', '0003_rename_id42_user_id_42_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.CharField(blank=True, default='https://res.cloudinary.com/dw9xon1xs/image/upload/v1699535128/nico_nk9vdi.jpg', max_length=255),
        ),
    ]