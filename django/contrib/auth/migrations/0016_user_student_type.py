# Generated by Django 5.0.6 on 2024-07-30 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0015_user_is_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='student_type',
            field=models.CharField(choices=[('all', 'مشترك كامل'), ('part', 'مشترك جزئي')], default='all', max_length=20, verbose_name='نوع اشتراك الطالب'),
        ),
    ]