from django.contrib import admin

from . import models as m

@admin.register(m.TempUser)
class TempUserAdmin(admin.ModelAdmin):
    ...