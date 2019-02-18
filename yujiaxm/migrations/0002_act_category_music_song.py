# Generated by Django 2.1.3 on 2019-01-13 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yujiaxm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Act',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='动作分类名称')),
                ('img', models.ImageField(default='', upload_to='img/', verbose_name='动作分类背景图片')),
            ],
            options={
                'verbose_name': '动作库',
                'verbose_name_plural': '动作库',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='分类名称')),
                ('title', models.CharField(max_length=30, verbose_name='标题')),
                ('people', models.IntegerField(verbose_name='参加人数')),
                ('img', models.ImageField(default='', upload_to='img/', verbose_name='分类图片')),
            ],
            options={
                'verbose_name': '课程分类',
                'verbose_name_plural': '课程分类',
            },
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='歌单分类名称')),
                ('img', models.ImageField(default='', upload_to='img/', verbose_name='歌单分类背景图片')),
            ],
            options={
                'verbose_name': '瑜伽音乐',
                'verbose_name_plural': '瑜伽音乐',
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='歌名')),
                ('t', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yujiaxm.Music', verbose_name='所属分类')),
            ],
            options={
                'verbose_name': '歌名',
                'verbose_name_plural': '歌名',
            },
        ),
    ]