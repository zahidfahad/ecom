from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ("title","image","is_active")
    list_display_links = ("title",'is_active',)
    list_filter = ('is_active',)
    list_per_page = 100
    list_max_show_all = 200
    inlines = ()


    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        form.base_fields['created_by'].initial = request.user
        form.base_fields['updated_by'].initial = request.user
        return form

