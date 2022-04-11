# Generated by Django 4.0.3 on 2022-04-11 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WXUser',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='用户的openid')),
                ('user_name', models.CharField(max_length=20, unique=True, verbose_name='用户名')),
                ('recent_choice', models.IntegerField(default=0, verbose_name='近期答对选择题数')),
                ('recent_cloze', models.IntegerField(default=0, verbose_name='近期答对完形小题数')),
                ('recent_reading', models.IntegerField(default=0, verbose_name='近期答对阅读小题数')),
                ('total_choice', models.IntegerField(default=0, verbose_name='做过的选择题总数')),
                ('right_choice', models.IntegerField(default=0, verbose_name='答对的选择题数')),
                ('total_cloze', models.IntegerField(default=0, verbose_name='做过的完形小题总数')),
                ('right_cloze', models.IntegerField(default=0, verbose_name='答对的完形小题数')),
                ('total_reading', models.IntegerField(default=0, verbose_name='做过的阅读题小题总数')),
                ('right_reading', models.IntegerField(default=0, verbose_name='做对的阅读题小题数')),
                ('status', models.IntegerField(default=0, verbose_name='刷题阶段')),
            ],
        ),
        migrations.AddConstraint(
            model_name='wxuser',
            constraint=models.CheckConstraint(check=models.Q(('recent_choice__gte', 0)), name='recent_choice__gte_0'),
        ),
        migrations.AddConstraint(
            model_name='wxuser',
            constraint=models.CheckConstraint(check=models.Q(('recent_cloze__gte', 0)), name='recent_cloze__gte_0'),
        ),
        migrations.AddConstraint(
            model_name='wxuser',
            constraint=models.CheckConstraint(check=models.Q(('recent_reading__gte', 0)), name='recent_reading__gte_0'),
        ),
        migrations.AddConstraint(
            model_name='wxuser',
            constraint=models.CheckConstraint(check=models.Q(('total_choice__gte', 0)), name='total_choice__gte_0'),
        ),
        migrations.AddConstraint(
            model_name='wxuser',
            constraint=models.CheckConstraint(check=models.Q(('right_choice__gte', 0)), name='right_choice__gte_0'),
        ),
        migrations.AddConstraint(
            model_name='wxuser',
            constraint=models.CheckConstraint(check=models.Q(('total_cloze__gte', 0)), name='total_cloze__gte_0'),
        ),
        migrations.AddConstraint(
            model_name='wxuser',
            constraint=models.CheckConstraint(check=models.Q(('right_cloze__gte', 0)), name='right_cloze__gte_0'),
        ),
        migrations.AddConstraint(
            model_name='wxuser',
            constraint=models.CheckConstraint(check=models.Q(('total_reading__gte', 0)), name='total_reading__gte_0'),
        ),
        migrations.AddConstraint(
            model_name='wxuser',
            constraint=models.CheckConstraint(check=models.Q(('right_reading__gte', 0)), name='right_reading__gte_0'),
        ),
        migrations.AddConstraint(
            model_name='wxuser',
            constraint=models.CheckConstraint(check=models.Q(('status', 0), ('status', 1), _connector='OR'), name='check_status'),
        ),
    ]
