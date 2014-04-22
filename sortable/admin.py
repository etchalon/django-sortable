from django.contrib import admin


class SortableAdmin(admin.ModelAdmin):
    # Make instances reorderable
    list_editable = ('position',)
    list_display = ('position', )

    class Media:
        js = ('js/django-admin-sortable.js',)
