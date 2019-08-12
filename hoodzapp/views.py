from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.http  import HttpResponse, Http404, HttpResponseRedirect
from registration.backends.simple.views import RegistrationView
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.db import transaction
from django.contrib import messages
from django.utils.translation import gettext as _

# Create your views here.
def index(request):
    return render(request, 'index.html')