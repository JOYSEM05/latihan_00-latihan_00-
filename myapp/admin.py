from django.db import models

from django.contrib import admin
from mynewapp.models import StatusModel  # impor model, bukan definisi ulang

admin.site.register(StatusModel)
