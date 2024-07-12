from django.contrib import admin
from .models import About, SocialMedia

# Register your models here.


class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count = About.objects.count()
        if count == 0:
            return True
        return False


class SocialMediaAdmin(admin.ModelAdmin):
    pass


admin.site.register(About, AboutAdmin)
admin.site.register(SocialMedia, SocialMediaAdmin)