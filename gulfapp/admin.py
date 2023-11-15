

# Register your models here.
from django.contrib import admin
from .models import ExcelData
from import_export.admin import ImportExportModelAdmin


@admin.register(ExcelData)
class ExcelDataAdmin(ImportExportModelAdmin):
    pass
