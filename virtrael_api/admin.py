# encoding=utf-8
'''

@author: Sergio Álvarez López

'''

from django.contrib import admin
from django.forms import ModelForm
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from models import *


admin.site.register(User)
admin.site.register(CarerPatient)
admin.site.register(TherapistPatient)
admin.site.register(Exerciseerror)
admin.site.register(Exerciselevel)
admin.site.register(Exerciseresult)
admin.site.register(Medal)
admin.site.register(Partialresult)
admin.site.register(Sessionlog)
admin.site.register(Userprofile)
admin.site.register(UserAvatar)