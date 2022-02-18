# Generated by Django 4.0.2 on 2022-02-18 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='branch_registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('branch_admin', models.CharField(max_length=100)),
                ('branch_type', models.CharField(max_length=100)),
                ('status', models.FileField(default='', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='create_team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('trainer', models.CharField(max_length=200)),
                ('progress', models.IntegerField()),
                ('status', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='internship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_date', models.DateField(max_length=200)),
                ('fullname', models.CharField(max_length=200)),
                ('collegename', models.CharField(max_length=200)),
                ('reg_no', models.CharField(max_length=200)),
                ('course', models.CharField(max_length=200)),
                ('stream', models.CharField(max_length=200)),
                ('platform', models.CharField(max_length=200)),
                ('start_date', models.CharField(max_length=200)),
                ('end_date', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=200)),
                ('alternative_no', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('profile_pic', models.ImageField(null=True, upload_to='')),
                ('attach_file', models.FileField(default='', upload_to='')),
                ('rating', models.CharField(max_length=200)),
                ('hrmanager', models.CharField(max_length=200)),
                ('guide', models.CharField(max_length=200)),
                ('qr', models.CharField(default='', max_length=200)),
                ('status', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('startdate', models.DateField(max_length=100)),
                ('enddate', models.DateField(max_length=100)),
                ('files', models.FileField(default='', upload_to='')),
                ('status', models.CharField(max_length=100)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='projectbranch', to='app.branch_registration')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='projectdepartment', to='app.branch_registration')),
            ],
        ),
        migrations.CreateModel(
            name='project_taskassign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=240)),
                ('description', models.TextField()),
                ('startdate', models.DateField(max_length=100)),
                ('enddate', models.DateField(max_length=100)),
                ('files', models.FileField(default='', upload_to='')),
                ('department', models.CharField(max_length=200)),
                ('designation', models.CharField(max_length=200)),
                ('employee', models.CharField(max_length=200)),
                ('tester', models.CharField(max_length=200)),
                ('extension', models.IntegerField()),
                ('reason', models.TextField()),
                ('extension_status', models.CharField(max_length=200)),
                ('tl_description', models.CharField(max_length=200)),
                ('submitted_date', models.DateField(max_length=100)),
                ('employee_files', models.FileField(default='', upload_to='')),
                ('employee_description', models.TextField()),
                ('status', models.CharField(max_length=200)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='project_taskassignproject', to='app.project')),
            ],
        ),
        migrations.CreateModel(
            name='user_registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=240, null=True)),
                ('fathername', models.CharField(max_length=240, null=True)),
                ('mothername', models.CharField(max_length=240, null=True)),
                ('dateofbirth', models.DateField(max_length=240, null=True)),
                ('gender', models.CharField(max_length=240, null=True)),
                ('presentaddress1', models.CharField(max_length=240, null=True)),
                ('presentaddress2', models.CharField(max_length=240, null=True)),
                ('presentaddress3', models.CharField(max_length=240, null=True)),
                ('pincode', models.CharField(max_length=240, null=True)),
                ('district', models.CharField(max_length=240, null=True)),
                ('state', models.CharField(max_length=240, null=True)),
                ('country', models.CharField(max_length=240, null=True)),
                ('permanentaddress1', models.CharField(max_length=240, null=True)),
                ('permanentaddress2', models.CharField(max_length=240, null=True)),
                ('permanentaddress3', models.CharField(max_length=240, null=True)),
                ('permanentpincode', models.CharField(max_length=240, null=True)),
                ('permanentdistrict', models.CharField(max_length=240, null=True)),
                ('permanentstate', models.CharField(max_length=240, null=True)),
                ('permanentcountry', models.CharField(max_length=240, null=True)),
                ('mobile', models.CharField(max_length=240, null=True)),
                ('alternativeno', models.CharField(max_length=240, null=True)),
                ('email', models.EmailField(max_length=240, null=True)),
                ('idproof', models.FileField(default='', upload_to='')),
                ('photo', models.FileField(default='', upload_to='')),
                ('designation', models.CharField(default='', max_length=240, null=True)),
                ('department', models.CharField(default='', max_length=240, null=True)),
                ('branch', models.CharField(default='', max_length=240, null=True)),
                ('team', models.CharField(default='', max_length=240, null=True)),
                ('attitude', models.PositiveIntegerField(default='')),
                ('creativity', models.PositiveIntegerField(default='')),
                ('workperformance', models.PositiveIntegerField(default='')),
                ('joiningdate', models.DateField(default='', max_length=240, null=True)),
                ('startdate', models.DateField(default='', max_length=240, null=True)),
                ('enddate', models.DateField(default='', max_length=240, null=True)),
                ('status', models.CharField(default='', max_length=240, null=True)),
                ('password', models.CharField(default='', max_length=240, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='trainer_task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trainee', models.CharField(max_length=240)),
                ('taskname', models.CharField(max_length=240)),
                ('startdate', models.DateField(max_length=100)),
                ('enddate', models.DateField(max_length=100)),
                ('files', models.FileField(default='', upload_to='')),
                ('description', models.TextField()),
                ('trainee_description', models.TextField()),
                ('trainee_files', models.FileField(default='', upload_to='')),
                ('status', models.CharField(max_length=200)),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='trainer_tasktrainer', to='app.user_registration')),
            ],
        ),
        migrations.CreateModel(
            name='topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=240)),
                ('startdate', models.DateField(max_length=100)),
                ('enddate', models.DateField(max_length=100)),
                ('files', models.FileField(default='', upload_to='')),
                ('description', models.TextField()),
                ('review', models.TextField()),
                ('status', models.CharField(max_length=200)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='topicteam', to='app.create_team')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='topictrainer', to='app.user_registration')),
            ],
        ),
        migrations.CreateModel(
            name='tester_status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(max_length=100)),
                ('workdone', models.TextField()),
                ('files', models.FileField(default='', upload_to='')),
                ('subtask', models.TextField()),
                ('progress', models.IntegerField()),
                ('status', models.CharField(max_length=200)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='tester_statusproject', to='app.project')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='tester_statustask', to='app.project_taskassign')),
                ('tester', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='tester_statustester', to='app.user_registration')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='tester_statususer', to='app.user_registration')),
            ],
        ),
        migrations.CreateModel(
            name='test_status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(max_length=100)),
                ('workdone', models.TextField()),
                ('files', models.FileField(default='', upload_to='')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='test_statusproject', to='app.project')),
                ('taskname', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='test_statustaskname', to='app.user_registration')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='test_statususer', to='app.user_registration')),
            ],
        ),
        migrations.CreateModel(
            name='reported_issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue', models.TextField()),
                ('reported_date', models.DateField(max_length=100)),
                ('reply', models.TextField()),
                ('status', models.CharField(max_length=200)),
                ('reported_to', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='reported_issuereported_to', to='app.user_registration')),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='reported_issuereporter', to='app.user_registration')),
            ],
        ),
        migrations.CreateModel(
            name='qualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plustwo', models.CharField(max_length=240, null=True)),
                ('schoolaggregate', models.CharField(max_length=240, null=True)),
                ('schoolcertificate', models.FileField(default='', upload_to='')),
                ('ugdegree', models.CharField(max_length=240, null=True)),
                ('ugstream', models.CharField(max_length=240, null=True)),
                ('ugpassoutyr', models.CharField(max_length=240, null=True)),
                ('ugaggregrate', models.CharField(max_length=240, null=True)),
                ('backlogs', models.CharField(max_length=240, null=True)),
                ('ugcertificate', models.FileField(default='', upload_to='')),
                ('pg', models.CharField(max_length=240, null=True)),
                ('status', models.CharField(default='', max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='qualificationuser', to='app.user_registration')),
            ],
        ),
        migrations.AddField(
            model_name='project_taskassign',
            name='tl',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='project_taskassigntl', to='app.user_registration'),
        ),
        migrations.AddField(
            model_name='project_taskassign',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='project_taskassignuser', to='app.user_registration'),
        ),
        migrations.AddField(
            model_name='project',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='projectuser', to='app.user_registration'),
        ),
        migrations.CreateModel(
            name='leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField(max_length=100)),
                ('to_date', models.DateField(max_length=100)),
                ('reason', models.TextField()),
                ('leave_status', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='leaveuser', to='app.user_registration')),
            ],
        ),
        migrations.CreateModel(
            name='extracurricular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internshipdetails', models.CharField(max_length=240, null=True)),
                ('internshipduration', models.CharField(max_length=240, null=True)),
                ('internshipcertificate', models.FileField(default='', upload_to='')),
                ('onlinetrainingdetails', models.CharField(max_length=240, null=True)),
                ('onlinetrainingduration', models.CharField(max_length=240, null=True)),
                ('onlinetrainingcertificate', models.FileField(default='', upload_to='')),
                ('projecttitle', models.CharField(max_length=240, null=True)),
                ('projectduration', models.CharField(max_length=240, null=True)),
                ('projectdescription', models.TextField(null=True)),
                ('projecturl', models.CharField(blank=True, default='', max_length=240, null=True)),
                ('skill1', models.CharField(blank=True, default='', max_length=240, null=True)),
                ('skill2', models.CharField(blank=True, default='', max_length=240, null=True)),
                ('skill3', models.CharField(blank=True, default='', max_length=240, null=True)),
                ('status', models.CharField(default='', max_length=240)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='extracurricularuser', to='app.user_registration')),
            ],
        ),
        migrations.CreateModel(
            name='designation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='designationbranch', to='app.branch_registration')),
            ],
        ),
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='departmentbranch', to='app.branch_registration')),
            ],
        ),
        migrations.CreateModel(
            name='attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(max_length=100)),
                ('status', models.CharField(max_length=200)),
                ('logintime', models.CharField(default='', max_length=200)),
                ('logouttime', models.CharField(default='', max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='attendanceuser', to='app.user_registration')),
            ],
        ),
    ]