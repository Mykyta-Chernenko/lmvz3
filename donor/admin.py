from django.contrib import admin
from django.contrib.auth.models import User
from django.http import QueryDict

from donor.models import Donor


@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    search_fields = ['name', 'surname', 'patronymic', 'birthday', 'pass_date', 'blood_group', 'rh', 'diseases']
    list_display = ['name', 'surname', 'patronymic', 'birthday', 'pass_date', 'blood_group', 'rh', 'diseases']
    list_filter = ['rh', 'blood_group']

    def changelist_view(self, request, extra_context=None):
        request.GET = request.GET.copy()
        type = request.GET.pop('type', [''])[0]
        name = request.GET.pop('_name', [''])[0]
        surname = request.GET.pop('_surname', [''])[0]
        patronymic = request.GET.pop('_patronymic', [''])[0]
        birthday = request.GET.pop('_birthday', [''])[0]
        blood_group = request.GET.pop('_blood_group', [''])[0]
        tr = request.GET.pop('_tr', [''])[0]
        pass_date = request.GET.pop('_pass_date', [''])[0]
        diseases = request.GET.pop('_diseases', [''])[0]
        _q = request.GET.pop('q', [''])[0]
        if type == 'elastic':
            q = _q
        else:
            q = (name + ' ' + surname + ' ' + patronymic + ' ' + birthday + ' ' + blood_group + ' ' + tr + ' ' + pass_date + ' ' + diseases).strip()
        if q:
            request.GET['q'] = q
        a = super(DonorAdmin, self).changelist_view(request, extra_context)
        a.context_data['search_name'] = name
        a.context_data['search_surname'] = surname
        a.context_data['search_patronymic'] = patronymic
        a.context_data['search_birthday'] = birthday
        a.context_data['search_blood_group'] = blood_group
        a.context_data['search_tr'] = tr
        a.context_data['search_pass_date'] = pass_date
        a.context_data['search_diseases'] = diseases
        if a.context_data['cl']:
            a.context_data['cl'].query = _q
        return a
