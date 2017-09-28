from django.views.generic.base import TemplateView
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
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
        return render(request, self.template_name, {
            'clients': self.__qs.filter(
                is_staff=False, is_superuser=False
            ), 'addresses': Address()
        })


class DataAddView(View):
    template_name = 'costomer/view_data_add.html'
    __context = dict()

    def post(self, request, *args, **kwargs):
        self.__create_context(request.user)
        return render(request, self.template_name, self.__context)

    def __create_context(self, user):
        if isinstance(user, AdminUser):
            self.__context.update(dict(form=ClientUserForm()))
        elif isinstance(user, StaffUser):
            self.__context.update()
        elif isinstance(user, CostomerServiceUser):
            self.__context.update()

    def __del__(self):
        pass


class DataUpdateView(View):
    pass


class DataDeleteView(View):
    pass
