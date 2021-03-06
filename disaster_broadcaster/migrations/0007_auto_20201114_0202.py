# Generated by Django 3.1.3 on 2020-11-14 02:02

import disaster_broadcaster.filepaths.FilePath
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('disaster_broadcaster', '0006_auto_20201114_0126'),
    ]

    operations = [
        migrations.CreateModel(
            name='CharityOrganization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200, unique=True)),
                ('address', models.CharField(default='', max_length=200)),
                ('url', models.URLField()),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('emergency_url', models.URLField(blank=True, null=True)),
                ('emergency_number', models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
            ],
        ),
        migrations.CreateModel(
            name='Disaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_happened', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DisasterCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=120)),
                ('guide_url', models.URLField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, default=None, max_length=1024)),
                ('content', models.FileField(null=True, upload_to=disaster_broadcaster.filepaths.FilePath.FilePath.post_upload)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('country_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='disaster_broadcaster.country')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reaction', models.CharField(choices=[(1, 'Like'), (2, 'Sad'), (3, 'Love')], default=3, max_length=3)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='disaster_broadcaster.post')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('date_created', models.DateTimeField(null=True)),
                ('headline', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('image', models.ImageField(null=True, upload_to=disaster_broadcaster.filepaths.FilePath.FilePath.news_upload)),
                ('country_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='disaster_broadcaster.country')),
                ('disaster_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='disaster_broadcaster.disaster')),
            ],
        ),
        migrations.CreateModel(
            name='Fund',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('disaster_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='disaster_broadcaster.disaster')),
                ('organization_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='disaster_broadcaster.charityorganization')),
            ],
        ),
        migrations.AddField(
            model_name='disaster',
            name='category_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='disaster_broadcaster.disastercategory'),
        ),
        migrations.AddField(
            model_name='disaster',
            name='country_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='disaster_broadcaster.country'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(blank=True, default=None, max_length=1024)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='disaster_broadcaster.post')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
