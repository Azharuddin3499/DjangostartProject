from django.contrib import admin
from services.models import Services
# Register your models here.

class ServicesAdmin(admin.ModelAdmin):
    list_display=('icon','title','description')

admin.site.register(Services,ServicesAdmin)