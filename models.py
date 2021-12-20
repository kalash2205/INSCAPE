# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class PatientsBills(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    date = models.DateTimeField()
    mcost = models.ForeignKey('PatientsMeds', models.DO_NOTHING, blank=True, null=True)
    owner = models.ForeignKey('PatientsPatient', models.DO_NOTHING, blank=True, null=True)
    rcost = models.ForeignKey('PatientsRooms', models.DO_NOTHING, blank=True, null=True)
    tcost = models.ForeignKey('PatientsTests', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patients_bills'


class PatientsMeds(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    mname = models.CharField(max_length=200)
    mcost = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'patients_meds'


class PatientsPatient(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    contact = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    id = models.CharField(primary_key=True, max_length=32)
    age = models.IntegerField(blank=True, null=True)
    sex = models.CharField(max_length=200, blank=True, null=True)
    arrival = models.DateTimeField()
    type = models.CharField(max_length=200, blank=True, null=True)
    treatment_category = models.ForeignKey('StaffSpecialities', models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'patients_patient'


class PatientsRooms(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    rno = models.IntegerField(blank=True, null=True)
    rcost = models.IntegerField(blank=True, null=True)
    owner = models.ForeignKey(PatientsPatient, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patients_rooms'


class PatientsTests(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    tname = models.CharField(max_length=200)
    tcost = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patients_tests'


class StaffDepartment(models.Model):
    dname = models.CharField(max_length=200)
    dno = models.CharField(primary_key=True, max_length=32)
    created = models.DateTimeField()
    dhead = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff_department'


class StaffSpecialities(models.Model):
    sname = models.CharField(max_length=200)
    sno = models.CharField(primary_key=True, max_length=32)
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'staff_specialities'


class StaffStaff(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    contact = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=500)
    staff_image = models.CharField(max_length=100, blank=True, null=True)
    id = models.CharField(primary_key=True, max_length=32)
    department = models.ForeignKey(StaffDepartment, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'staff_staff'
