from django.views.generic.base import TemplateView
from django.views import View
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from users.models import AdminUser, StaffUser, CostomerServiceUser
from users.models import ClientUser, Address
from users.forms import ClientUserForm, AddressForm


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        return super(self.__class__, self).get_context_data(**kwargs)


class HomeLoginView(TemplateView):
    template_name = 'views/home.html'


class DataView(View):
    template_name = 'costomer/view_data.html'
    __context = dict()
    __qs = ClientUser.objects.all()

    def get(self, request, *args, **kwargs):
        if request.user.has_perms(
            'users.add_clientuser',
            'users.change_clientuser', 'users.delete_clientuser'
        ):
            return render(request, self.template_name, {
                'clients': self.__qs.filter(
                    is_staff=False, is_superuser=False
                ),
                'addresses': Address.objects.all()
            })
        if not request.user.has_perms(
            'users.change_clientuser', 'users.delete_clientuser'
        ) and request.user.has_perms('view_address'):
            return render(request, self.template_name, {
                'permissions':  'view_address',
                'addresses': Address.objects.all()
            })


class DataAddView(View):
    template_name = 'costomer/view_data_add.html'
    __context = dict()

    def post(self, request, *args, **kwargs):
        self.__create_context(request.user)
        return render(request, self.template_name, self.__context)

    def get(self, request, *args, **kwargs):
        self.__create_context(request.user)
        return render(request, self.template_name, self.__context)

    def __create_context(self, user):
        if user.is_superuser and user.is_staff:
            self.__context = {
                'formclient': ClientUserForm(),
                'formaddress': AddressForm()
            }
        elif user.is_staff and not user.is_superuser:
            self.__context.update({
                'formaddress': AddressForm()
            })
            self.__context.update()
        elif user.has_perms('view_address'):
            self.__context.update()

    def __del__(self):
        pass


class DataUpdateView(View):
    template_name = 'costomer/view_data_update.html'
    __context = dict()

    def get(self, request, clientid, *args, **kwargs):
        self.__create_context(request.user, clientid)
        return render(request, self.template_name, self.__context)

    def post(self, request, clientid, *args, **kwargs):
        try:
            client = ClientUser.objects.get(pk=clientid)
            address = Address.objects.get(user=client)
        except ObjectDoesNotExist as e:
            pass
        except MultipleObjectsReturned as e:
            pass

        clientForm = ClientUserForm(request.POST, instance=client)
        addressForm = AddressForm(
            request.POST, instance=Address(user=client, pk=address.id)
        )
        if clientForm.is_valid() and addressForm.is_valid():
            clientForm.save()
            addressForm.save()
            return HttpResponseRedirect('/costomer/data/')

        return render(request, self.template_name, self.__context)

    def __create_context(self, user, clientid):
        try:
            client = ClientUser.objects.get(pk=clientid)
            address = Address.objects.get(user=client)
        except ObjectDoesNotExist as e:
            pass
        except MultipleObjectsReturned as e:
            pass

        clientForm = ClientUserForm(request.POST, instance=client)
        addressForm = AddressForm(
            request.POST, instance=Address(user=client, pk=address.id)
        )

        if user.is_superuser and user.is_staff:
            self.__context = {
                'formclient': clientForm,
                'formaddress': addressForm
            }
        elif user.is_staff and not user.is_superuser:
            self.__context.update({
                'formaddress': addressForm
            })
            self.__context.update()
        elif user.has_perms('view_address') and not user.has_perms(
            'change_address'
        ):
            self.__context = {}


class DataDeleteView(View):
    template_name = 'costomer/view_data_delete.html'
