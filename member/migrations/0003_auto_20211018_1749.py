# Generated by Django 3.2.7 on 2021-10-18 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_alter_users_uage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='uact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='member.activity', verbose_name='활동량'),
        ),
        migrations.AlterField(
            model_name='users',
            name='uage',
            field=models.IntegerField(verbose_name='나이'),
        ),
        migrations.AlterField(
            model_name='users',
            name='uheight',
            field=models.FloatField(verbose_name='키'),
        ),
        migrations.AlterField(
            model_name='users',
            name='upw',
            field=models.CharField(max_length=15, verbose_name='비밀번호'),
        ),
        migrations.AlterField(
            model_name='users',
            name='urdc',
            field=models.FloatField(verbose_name='권장칼로리'),
        ),
        migrations.AlterField(
            model_name='users',
            name='usex',
            field=models.CharField(choices=[['F', '여성'], ['M', '남성 ']], max_length=1, verbose_name='성별'),
        ),
        migrations.AlterField(
            model_name='users',
            name='uuid',
            field=models.EmailField(max_length=254, primary_key=True, serialize=False, verbose_name='이메일'),
        ),
        migrations.AlterField(
            model_name='users',
            name='uweight',
            field=models.FloatField(verbose_name='몸무게'),
        ),
    ]
