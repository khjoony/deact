from django.contrib import admin
from .models import Kosdak, KosdakInstance, Kospi, KospiInstance, Owner, Sector
# Register your models here.

admin.site.register(Sector)
## admin.site.register(Kospi)
## admin.site.register(Kosdak)

##  Define Inline model
class KospisInline(admin.TabularInline):
    model = Kospi
class KosdaksInline(admin.TabularInline):
    model = Kosdak


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [KospisInline, KosdaksInline]

## Define Inline modelinstance
class KospisInstanceInline(admin.TabularInline):
    model = KospiInstance
class KosdaksInstanceInline(admin.TabularInline):
    model = KosdakInstance


class KospiAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'display_sector')
    inlines = [KospisInstanceInline]

class KosdakAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'display_sector')
    inlines = [KosdaksInstanceInline]

admin.site.register(Kospi, KospiAdmin)
admin.site.register(Kosdak, KosdakAdmin)



@admin.register(KospiInstance)
class KospiInstanceAdmin(admin.ModelAdmin):
    list_display = ('kospi', 'status', 'user', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields':('kospi', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'user')
        }),
    )

@admin.register(KosdakInstance)
class KosdakInstanceAdmin(admin.ModelAdmin):
    list_display = ('kosdak', 'status', 'user', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields':('kosdak', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'user')
        }),
    )