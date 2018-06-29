from django.contrib import admin
from reports.models import Category, Report, Answer, Label


@admin.register(Category)
class GroupAdmin(admin.ModelAdmin):
    pass


@admin.register(Report)
class GroupAdmin(admin.ModelAdmin):
    pass


@admin.register(Answer)
class GroupAdmin(admin.ModelAdmin):
    pass


@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    pass