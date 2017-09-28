from django.forms import ModelForm
from users.models import ClientUser, Address


class ClientUserForm(ModelForm):

    class Meta:
        model = ClientUser
        fields = '__all__'
        exclude = [
            'groups', 'user_permissions', 'is_staff', 'is_superuser',
            'last_login', 'date_joined'
        ]


class AddressForm(ModelForm):

    class Meta:
        model = Address
        fields = '__all__'
