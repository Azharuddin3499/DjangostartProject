from django.contrib import admin
from comments.models import Comments
# Register your models here.
class SaveComments(admin.ModelAdmin):
    list_display=('name','comment')
admin.site.register(Comments,SaveComments)