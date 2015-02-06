# encoding=utf-8
'''

@author: Sergio Álvarez López
'''
# Versión inferior a 1.6
# from django.conf.urls.defaults import *
# versión superior a 1.6
import random
import logging

from django.conf.urls import *
from django.db.models import Q, Count
from tastypie.authorization import Authorization, DjangoAuthorization
from tastypie.authentication import SessionAuthentication
from tastypie.resources import ModelResource, Resource
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie import fields
from tastypie.utils import trailing_slash
from django.core.paginator import Paginator, InvalidPage
from django.http import Http404
import simplejson
from django.db import DatabaseError

from models import *
import sys

import hashlib

from django.contrib.auth.models import Group
from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from tastypie.http import HttpUnauthorized, HttpForbidden


logger = logging.getLogger(__name__)


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        fields = ['first_name', 'last_name', 'email']
        allowed_methods = ['get', 'post']
        resource_name = 'user'

    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/login%s$" %
                (self._meta.resource_name, trailing_slash()), self.wrap_view('login'), name="api_login"),
            url(r'^(?P<resource_name>%s)/logout%s$' %
                (self._meta.resource_name, trailing_slash()), self.wrap_view('logout'), name='api_logout'),
        ]

    def login(self, request, **kwargs):
        self.method_check(request, allowed=['post'])

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return self.create_response(request, {
                    'success': True,
                    'cookies': request.COOKIES,})
            else:
                return self.create_response(request, {
                    'success': False,
                    'reason': 'disabled',
                    }, HttpForbidden )
        else:
            return self.create_response(request, {
                'success': False,
                'reason': 'incorrect',
                }, HttpUnauthorized )

    def logout(self, request, **kwargs):
        self.method_check(request, allowed=['get'])
        if request.user and request.user.is_authenticated():
            logout(request)
            return self.create_response(request, { 'success': True })
        else:
            return self.create_response(request, { 'success': False }, HttpUnauthorized)

class ExerciseErrorResource(ModelResource):
    '''
        
    '''
    class Meta:
        queryset = Exerciseerror.objects.all()
        resource_name = 'exercise_error'

