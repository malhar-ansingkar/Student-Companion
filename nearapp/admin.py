from .models import college, shop, PostImage, suggestions, faqs
from django.contrib import admin
from django_admin_listfilter_dropdown.filters import (
    DropdownFilter, ChoiceDropdownFilter, RelatedDropdownFilter)
# Register your models here.


class modelClass(admin.ModelAdmin):
    list_filter = [
        ("Type", DropdownFilter),
        ("college", RelatedDropdownFilter),
    ]

    class Meta:
        model = shop


class ImagesClass(admin.ModelAdmin):
    list_filter = [
        ("post", RelatedDropdownFilter),
        # ("post.college", DropdownFilter),
    ]

    class Meta:
        model = shop
# admin.site.unregister(shop)


admin.site.register(college)
admin.site.register(PostImage, ImagesClass)
admin.site.register(shop, modelClass)

admin.site.register(suggestions)
admin.site.register(faqs)

# admin.site.register(shopDetails)
