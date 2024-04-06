# Generated by Django 3.0 on 2023-11-02 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('myshop', '0005_auto_20231102_0845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='customuser_set', related_query_name='customuser', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(help_text='Specific permissions for this user.', related_name='customuser_set', related_query_name='customuser', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='qty',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='qty',
            field=models.IntegerField(),
        ),
    ]
