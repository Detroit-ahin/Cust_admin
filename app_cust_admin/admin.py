from django.contrib import admin
from .models import User_list
from .actions import create_duplicate_action 

# Register your models here.
class HomeAdmin(admin.ModelAdmin):
    #for display the data in a list view
    list_display = ('fullname', 'app_id','profession','email','status')

    #filter your data as you want
    list_filter = ['profession']

    #search fileds
    search_fields = ['fullname','keyword']

    #edit value on admin panel directly
    list_editable = ("profession","email")

    #link action with Homeadmin class
    actions = [create_duplicate_action()]


admin.site.register(User_list,HomeAdmin)

admin.site.site_header = "Django admin Customization"
