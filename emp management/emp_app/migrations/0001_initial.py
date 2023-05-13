# Generated by Django 3.2.12 on 2023-02-08 06:15

from django.db import migrations, models
import emp_app.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='leaveinformation',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('managername', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('applyleave', models.IntegerField(null=True)),
                ('leavepurpose', models.CharField(max_length=200)),
                ('leavedatefrom', models.DateField(null=True)),
                ('leavedateto', models.DateField(null=True)),
                ('leavestatus', models.CharField(default='pending', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Userdetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('employeename', models.CharField(max_length=100)),
                ('employeepic', models.ImageField(upload_to='images/')),
                ('fathername', models.CharField(max_length=100)),
                ('mothername', models.CharField(max_length=100)),
                ('employeeid', models.CharField(max_length=100)),
                ('employeedegination', models.CharField(max_length=200)),
                ('joiningdate', models.DateField(null=True)),
                ('employeeleave', models.IntegerField(null=True)),
                ('employeesalary', models.IntegerField(null=True)),
                ('employeecontect', models.IntegerField(null=True)),
                ('employeeaddress', models.CharField(max_length=200)),
                ('Key', models.CharField(max_length=200, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', emp_app.manager.CustomuserdetailManager()),
            ],
        ),
    ]
