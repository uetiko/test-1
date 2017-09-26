from django.contrib import admin
from users.models import AdminUser, StaffUser, CostomerServiceUser
from users.models import ClientUser
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserSystemAdmin(BaseUserAdmin):
    '''
        Admin View for User
    '''
    list_display = ('get_username', 'email')
    list_filter = ('email',)
    search_fields = ['email']
admin.site.register(AdminUser, UserSystemAdmin)


class StaffAdmin(BaseUserAdmin):
    '''
        Admin View for Staff
    '''
    list_display = ('get_username', 'email')
    list_filter = ('email',)
    search_fields = ['email']

    def get_queryset(self, request):
        qs = super(self.__class__, self).get_queryset(request)
        return qs.filter(is_staff=True, is_superuser=False)

admin.site.register(StaffUser, StaffAdmin)


class CostomerServiceUserAdmin(BaseUserAdmin):
    '''
        Admin View for CostomerServiceUser
    '''
    list_display = ('get_username', 'email')
    list_filter = ('email',)
    search_fields = ['email']
admin.site.register(CostomerServiceUser, CostomerServiceUserAdmin)


class ClientUserAdmin(admin.ModelAdmin):
    '''
        Admin View for ClientUser
    '''
    list_display = ('get_username', 'email')
    list_filter = ('email',)
    search_fields = ['email']

    def get_queryset(self, request):
        qs = super(self.__class__, self).get_queryset(request)
        return qs.filter(is_staff=False, is_superuser=False)

admin.site.register(ClientUser, ClientUserAdmin)
