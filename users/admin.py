from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import Resume, CustomUser
admin.site.register(Resume)


# class HiddenModelAdmin(admin.ModelAdmin):
#     def get_model_perms(self, *args, **kwargs):
#         perms = admin.ModelAdmin.get_model_perms(self, *args, **kwargs)
#         perms['isDeleted'] = True
#         return perms

@admin.register(CustomUser)
class UserAdmin(DjangoUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    exclude = ('isDeleted',)

    def get_queryset(self, request):
        qs = self.model.objects.filter(isDeleted=False)
        ordering = self.get_ordering(request)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs
