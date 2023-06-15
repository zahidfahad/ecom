from django.contrib import admin
from .models import *

# Register your models here.

class InlineProductImages(admin.TabularInline):
    model = ProductImage
    min_num = 0
    max_num = 5
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title","category","sub_category")
    list_display_links = ("title","category","sub_category")
    list_filter = ("category","sub_category")
    list_select_related = False
    list_per_page = 100
    list_max_show_all = 200
    list_editable = ()
    search_fields = ()
    search_help_text = "title"
    inlines = [InlineProductImages]
    
    
    @admin.display(description="Category")
    def category(self):
        return self.category.name
    
    @admin.display(description="Sub Category")
    def sub_category(self):
        return self.sub_category.name
    
    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        form.base_fields['created_by'].initial = request.user
        form.base_fields['updated_by'].initial = request.user
        return form
    
    
    
    

class InlineSubCategory(admin.TabularInline):
    model = SubCategory
    min_num = 0
    max_num = 5
    extra = 1
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name","is_active")
    list_display_links = ("name","is_active")
    list_filter = ("is_active",)
    list_select_related = False
    list_per_page = 100
    list_max_show_all = 200
    list_editable = ()
    search_fields = ()
    search_help_text = "title"
    inlines = [InlineSubCategory]
    

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        form.base_fields['created_by'].initial = request.user
        form.base_fields['updated_by'].initial = request.user
        return form