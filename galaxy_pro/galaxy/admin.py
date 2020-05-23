from django.contrib import admin
from .models import Servers,Request

# Register your models here.
class CloudServers(admin.ModelAdmin):

    list_dipslay=('__str__','ip')

admin.site.register(Servers,CloudServers)
admin.site.register(Request,CloudServers)
