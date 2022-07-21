from django.contrib import admin
from .models import reservationModel, Menu, MenuReservation, Review

from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin


class MenuAdmin(ImportExportMixin, admin.ModelAdmin):
    pass


admin.site.register(reservationModel)
admin.site.register(MenuReservation)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Review)
