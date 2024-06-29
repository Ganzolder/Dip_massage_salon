from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.dateparse import parse_datetime
from django.views.generic import DetailView, TemplateView, CreateView, UpdateView, DeleteView, ListView

from service.forms import ApppointmentForm, ServicesForm
from service.models import Services, Apppointment
from django.utils.timezone import make_aware


class IndexView(TemplateView):
    template_name = 'service/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        top_services = Services.objects.filter(top_service=True)
        context['top_services'] = top_services
        return context


class ApppointmentCreateView(CreateView):
    model = Apppointment
    form_class = ApppointmentForm
    success_url = reverse_lazy('service:apppointment_form_success')

    def get_initial(self):
        initial = super().get_initial()
        service_id = self.kwargs.get('service_id')
        if service_id:
            initial['service'] = service_id
        return initial

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        self.object = form.save(commit=False)

        if self.request.user.is_authenticated:
            self.object.creator = self.request.user
        else:
            self.object.creator = None

        start_at_str = self.request.POST.get('date')

        if start_at_str:
            start_at = parse_datetime(start_at_str)
            self.object.start_at = make_aware(start_at)
        else:
            form.add_error('date', 'Заполните поле даты и времени.')
            return self.form_invalid(form)

        self.object.save()

        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):

        context_data = super().get_context_data(**kwargs)
        return context_data


class ApppointmentFormSuccessView(TemplateView):
    template_name = 'service/apppointment_form_success.html'


class ApppointmentDetailView(DetailView):
    model = Apppointment
    template_name = 'main/apppointment_detail.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        return context_data


class ApppointmentUpdateView(PermissionRequiredMixin, UpdateView):
    model = Apppointment
    form_class = ApppointmentForm
    success_url = reverse_lazy('service:app_list')
    permission_required = 'change_appointment'

    def get_initial(self):
        initial = super().get_initial()

        service_id = self.kwargs.get('service_id')

        if service_id:
            initial['service'] = service_id
        return initial

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()

        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        self.object = form.save(commit=False)

        self.object.creator = self.request.user

        # Получаем новое значение date из POST запроса
        new_date_str = self.request.POST.get('date')

        if new_date_str:
            new_date = parse_datetime(new_date_str)
            self.object.date = make_aware(new_date)

        self.object.save()

        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):

        context_data = super().get_context_data(**kwargs)

        return context_data


class ApppointmentDeleteView(LoginRequiredMixin, DeleteView):
    model = Apppointment

    def post(self, request, *args, **kwargs):
        # Получаем объект по первичному ключу (pk)
        obj = get_object_or_404(Apppointment, pk=kwargs['pk'])

        if request.user.is_superuser:
            obj.delete()
            return redirect('service:app_list')
        if obj.creator == request.user:
            obj.delete()
            return redirect('users:user_detail')
        else:
            return redirect('users:user_detail')


class ApppointmentConfirmDeleteView(LoginRequiredMixin, TemplateView):
    template_name = 'service/apppointment_confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = get_object_or_404(Apppointment, pk=kwargs['pk'])
        return context


class ApppointmentListAdminView(PermissionRequiredMixin, ListView):

    template_name = 'service/apppointment_list.html'
    model = Apppointment
    permission_required = 'view_admin_list_app'

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['objects_list'] = Apppointment.objects.all().order_by('date')
        return context_data


class ServicesCreateView(PermissionRequiredMixin, CreateView):
    model = Services
    form_class = ServicesForm
    success_url = reverse_lazy('service:services_list')
    permission_required = 'create_services'

    def form_valid(self, form):
        self.object = form.save()
        self.object.creator = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)
        # context_data['objects_list'] = Services.objects.filter(creator=self.request.user).order_by('-enabled')
        context_data['title'] = f'Создание услуги'
        # context_data['object_type'] = 'message'

        return context_data


class ServicesListView(ListView):
    template_name = 'service/services_list.html'

    model = Services

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['objects_list'] = Services.objects.all()
        context_data['title'] = f'Наши услуги'
        return context_data


class ServicesUpdateView(PermissionRequiredMixin, UpdateView):
    model = Services
    form_class = ServicesForm
    success_url = reverse_lazy('service:services_list')
    permission_required = 'change_services'

    def form_valid(self, form):
        self.object = form.save()
        self.object.creator = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = f'Изменить услугу'

        return context_data


class ServicesDetailView(DetailView):
    model = Services
    template_name = 'service/services_detail.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        service = self.get_object()

        context_data['title'] = service.title
        context_data['content'] = service.content
        context_data['image'] = service.image
        context_data['price'] = service.price
        context_data['top_service'] = service.top_service

        return context_data


class ServicesDeleteView(PermissionRequiredMixin, DeleteView):
    model = Services
    permission_required = 'delete_services'

    def post(self, request, *args, **kwargs):
        # Получаем объект по первичному ключу (pk)
        obj = get_object_or_404(Services, pk=kwargs['pk'])

        # Удаляем объект
        obj.delete()

        # Перенаправляем на нужную страницу после удаления
        return redirect('service:services_list')


class ServicesConfirmDeleteView(PermissionRequiredMixin, TemplateView):
    template_name = 'service/services_confirm_delete.html'
    permission_required = 'delete_services'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = get_object_or_404(Services, pk=kwargs['pk'])
        return context
