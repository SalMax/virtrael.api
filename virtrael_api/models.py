# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255)
    hashedpassword = models.CharField(db_column='hashedPassword', max_length=255) # Field name made lowercase.
    admin = models.IntegerField()
    therapist = models.IntegerField()
    carer = models.IntegerField()
    activationkey = models.CharField(db_column='activationKey', max_length=100) # Field name made lowercase.
    status = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'user'

class CarerPatient(models.Model):
    carer = models.OneToOneField('User', related_name='carer_id', primary_key=True)
    patient = models.OneToOneField('User', related_name='patient_carer', primary_key=True)
    class Meta:
        managed = False
        db_table = 'carer_patient'

class TherapistPatient(models.Model):
    therapist = models.OneToOneField('User', related_name='therapist_id', primary_key=True)
    patient = models.ForeignKey('User', related_name='patient_therapist')
    class Meta:
        managed = False
        db_table = 'therapist_patient'

class Exerciseerror(models.Model):
    id = models.IntegerField(primary_key=True)
    sessionid = models.IntegerField(db_column='sessionID') # Field name made lowercase.
    exerciseid = models.IntegerField(db_column='exerciseID') # Field name made lowercase.
    userid = models.IntegerField(db_column='userID') # Field name made lowercase.
    errorkey = models.IntegerField(db_column='errorKey') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'exerciseError'

class Exerciselevel(models.Model):
    id = models.IntegerField(primary_key=True)
    userid = models.IntegerField(db_column='userID') # Field name made lowercase.
    exercisetype = models.IntegerField(db_column='exerciseType') # Field name made lowercase.
    userlevel = models.IntegerField(db_column='userLevel') # Field name made lowercase.
    usersublevel = models.IntegerField(db_column='userSubLevel') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'exerciseLevel'

class Exerciseresult(models.Model):
    id = models.IntegerField(primary_key=True)
    sessionid = models.IntegerField(db_column='sessionID') # Field name made lowercase.
    exerciseid = models.IntegerField(db_column='exerciseID') # Field name made lowercase.
    userid = models.IntegerField(db_column='userID') # Field name made lowercase.
    countcorrects = models.IntegerField(db_column='countCorrects') # Field name made lowercase.
    countfails = models.IntegerField(db_column='countFails') # Field name made lowercase.
    countomissions = models.IntegerField(db_column='countOmissions') # Field name made lowercase.
    finalscore = models.IntegerField(db_column='finalScore') # Field name made lowercase.
    seconds = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'exerciseResult'

class Medal(models.Model):
    id = models.IntegerField(primary_key=True)
    kindofmedal = models.IntegerField(db_column='kindOfMedal') # Field name made lowercase.
    date = models.DateTimeField()
    sessionid = models.IntegerField(db_column='sessionID') # Field name made lowercase.
    exerciseid = models.IntegerField(db_column='exerciseID') # Field name made lowercase.
    userid = models.IntegerField(db_column='userID') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'medal'

class Partialresult(models.Model):
    userid = models.IntegerField(db_column='userID') # Field name made lowercase.
    sessionid = models.IntegerField(db_column='sessionID') # Field name made lowercase.
    exerciseid = models.IntegerField(db_column='exerciseID') # Field name made lowercase.
    exercisetype = models.IntegerField(db_column='exerciseType') # Field name made lowercase.
    repetition = models.IntegerField()
    entry = models.TextField()
    class Meta:
        managed = False
        db_table = 'partialResult'

class Sessionlog(models.Model):
    id = models.IntegerField(primary_key=True)
    sessionid = models.IntegerField(db_column='sessionID') # Field name made lowercase.
    exerciseid = models.IntegerField(db_column='exerciseID') # Field name made lowercase.
    userid = models.IntegerField(db_column='userID') # Field name made lowercase.
    starttime = models.DateTimeField(db_column='startTime') # Field name made lowercase.
    endtime = models.DateTimeField(db_column='endTime') # Field name made lowercase.
    repetitions = models.IntegerField()
    result = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'sessionlog'





class Userprofile(models.Model):
    id = models.IntegerField(primary_key=True)
    userid = models.IntegerField(db_column='userID') # Field name made lowercase.
    placeofbirth = models.CharField(db_column='placeOfBirth', max_length=200) # Field name made lowercase.
    phonenumber = models.CharField(db_column='phoneNumber', max_length=30) # Field name made lowercase.
    sex = models.IntegerField()
    dateofbirth = models.DateField(db_column='dateOfBirth') # Field name made lowercase.
    civilstatus = models.IntegerField(db_column='civilStatus') # Field name made lowercase.
    partner = models.IntegerField()
    levelofstudies = models.IntegerField(db_column='levelOfStudies') # Field name made lowercase.
    hoursreading = models.IntegerField(db_column='hoursReading') # Field name made lowercase.
    hoursworkshop = models.IntegerField(db_column='hoursWorkshop') # Field name made lowercase.
    hoursexercise = models.IntegerField(db_column='hoursExercise') # Field name made lowercase.
    hourscomputer = models.IntegerField(db_column='hoursComputer') # Field name made lowercase.
    eatinghelp = models.IntegerField(db_column='eatingHelp') # Field name made lowercase.
    washinghelp = models.IntegerField(db_column='washingHelp') # Field name made lowercase.
    clothinghelp = models.IntegerField(db_column='clothingHelp') # Field name made lowercase.
    smartenuphelp = models.IntegerField(db_column='smartenUPHelp') # Field name made lowercase.
    urinatehelp = models.IntegerField(db_column='urinateHelp') # Field name made lowercase.
    defecatehelp = models.IntegerField(db_column='defecateHelp') # Field name made lowercase.
    toilethelp = models.IntegerField(db_column='toiletHelp') # Field name made lowercase.
    movinghelp = models.IntegerField(db_column='movingHelp') # Field name made lowercase.
    walkinghelp = models.IntegerField(db_column='walkingHelp') # Field name made lowercase.
    stepshelp = models.IntegerField(db_column='stepsHelp') # Field name made lowercase.
    phonehelp = models.IntegerField(db_column='phoneHelp') # Field name made lowercase.
    shoppinghelp = models.IntegerField(db_column='shoppingHelp') # Field name made lowercase.
    cookinghelp = models.IntegerField(db_column='cookingHelp') # Field name made lowercase.
    homecarehelp = models.IntegerField(db_column='homecareHelp') # Field name made lowercase.
    clothcleaninghelp = models.IntegerField(db_column='clothCleaningHelp') # Field name made lowercase.
    transporthelp = models.IntegerField(db_column='transportHelp') # Field name made lowercase.
    medicationhelp = models.IntegerField(db_column='medicationHelp') # Field name made lowercase.
    economyhelp = models.IntegerField(db_column='economyHelp') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'userProfile'

class UserAvatar(models.Model):
    user = models.ForeignKey(User, primary_key=True)
    avatar = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'user_avatar'

