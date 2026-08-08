from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json
from django.views.decorators.csrf import csrf_exempt

from .populate import initiate

logger = logging.getLogger(__name__)


@csrf_exempt
def login_user(request):
    data = json.loads(request.body)

    username = data["userName"]
    password = data["password"]

    user = authenticate(username=username, password=password)

    response = {"userName": username}

    if user is not None:
        login(request, user)
        response = {
            "userName": username,
            "status": "Authenticated"
        }

    return JsonResponse(response)
