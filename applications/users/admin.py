from django.contrib import admin
from users.models import AdminUser, StaffUser, CostomerServiceUser
from users.models import ClientUser, Address
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class AddressInline(admin.TabularInline):
    '''
    Tabular Inline View for Address
    '''
    model = Address
    min_num = 1
    max_num = 20
    extra = 0


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
    inlines = [AddressInline]
    list_filter = ('email',)
    search_fields = ['email']

    def get_queryset(self, request):
        qs = super(self.__class__, self).get_queryset(request)
        return qs.filter(is_staff=False, is_superuser=False)

admin.site.register(ClientUser, ClientUserAdmin)


class AddressAdmin(admin.ModelAdmin):
    '''
        Admin View for Address
    '''
    list_display = ('state', 'suburb')
    list_filter = ('state', 'suburb', 'municipality')
    search_fields = ['state', 'suburb', 'municipality']
admin.site.register(Address, AddressAdmin)
