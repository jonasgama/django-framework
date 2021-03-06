# Generated by Django 3.2.8 on 2021-10-13 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_alter_contact_creation_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Contact', 'verbose_name_plural': 'Contacts'},
        ),
        migrations.AddField(
            model_name='contact',
            name='enable',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='rate',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='update_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default='', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterUniqueTogether(
            name='contact',
            unique_together={('name', 'category')},
        ),
    ]
