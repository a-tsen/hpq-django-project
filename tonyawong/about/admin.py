from django.contrib import admin

from .models import About


class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False if self.model.objects.count() > 0 else super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False if self.model.objects.count() > 0 else super().has_add_permission(request)


admin.site.register(About, AboutAdmin)
