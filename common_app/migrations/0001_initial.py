# Generated by Django 5.0.6 on 2025-07-07 15:26

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='common_app_customuser_set', related_query_name='common_app_customuser', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='common_app_customuser_permissions', related_query_name='common_app_customuser', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=255)),
                ('contact_person', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('industry', models.CharField(blank=True, max_length=100, null=True)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='client_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=20, unique=True)),
                ('date_of_hire', models.DateField()),
                ('department', models.CharField(max_length=100)),
                ('job_title', models.CharField(max_length=100)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team_members', to='common_app.employee')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='employee_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
            },
        ),
        migrations.CreateModel(
            name='LeaveRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leave_type', models.CharField(choices=[('sick', 'Sick Leave'), ('casual', 'Casual Leave'), ('vacation', 'Vacation Leave'), ('maternity', 'Maternity Leave'), ('paternity', 'Paternity Leave'), ('unpaid', 'Unpaid Leave')], max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('reason', models.TextField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected'), ('cancelled', 'Cancelled')], default='pending', max_length=20)),
                ('requested_at', models.DateTimeField(auto_now_add=True)),
                ('response_at', models.DateTimeField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('approved_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='approved_leave_requests', to=settings.AUTH_USER_MODEL)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leave_requests', to='common_app.employee')),
            ],
            options={
                'verbose_name': 'Leave Request',
                'verbose_name_plural': 'Leave Requests',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('planning', 'Planning'), ('in_progress', 'In Progress'), ('completed', 'Completed'), ('on_hold', 'On Hold'), ('cancelled', 'Cancelled')], default='planning', max_length=20)),
                ('budget', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='common_app.client')),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='managed_projects', to='common_app.employee')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('to_do', 'To Do'), ('in_progress', 'In Progress'), ('done', 'Done'), ('blocked', 'Blocked')], default='to_do', max_length=20)),
                ('priority', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High'), ('urgent', 'Urgent')], default='medium', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_tasks', to='common_app.employee')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='common_app.project')),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
            },
        ),
    ]
