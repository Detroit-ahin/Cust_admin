import csv
from django.http import HttpResponse
from datetime import datetime
from .models import User_list
from django.contrib import messages

def create_duplicate_action():

    def create_duplicate(modeladmin, request, queryset):
        if len(queryset) > 1:
            messages.error(request , "Can not select more than one lead.")
        else:
            obj = queryset.values('fullname', 'app_id','profession','email','status')[0]
            obj['status'] = 1
            User_list.objects.create(**obj)
            messages.info(request, "Successfully created duplicate lead.")
        return True

    create_duplicate.short_description = "Create Duplicate User"
    return create_duplicate

