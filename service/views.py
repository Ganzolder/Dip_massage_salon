from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

import datetime as dt

from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.dateparse import parse_datetime
from django.views.generic import DetailView, TemplateView, CreateView, UpdateView, DeleteView, ListView

from service.forms import ApppointmentForm, ServicesForm
from service.models import Services, Apppointment
from django.utils.timezone import make_aware

from users.models import User


class IndexView(TemplateView):
    template_name = 'service/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        '''context['num_recipients'] = Recipient.objects.filter(creator=user).count()
        context['num_messages'] = Message.objects.filter(creator=user).count()
        context['num_posts'] = Post.objects.filter(creator=user).count()'''
        return context


class ApppointmentCreateView(CreateView):
    model = Apppointment
    form_class = ApppointmentForm
    success_url = reverse_lazy('service:index')
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.creator = self.request.user

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
    '''context_data['objects_list'] = Post.objects.filter(creator=self.request.user).order_by('-enabled')
        context_data['title'] = f'Список рассылок в базе'
        context_data['object_type'] = 'post'''


class ApppointmentDetailView(DetailView):
    model = Apppointment
    template_name = 'main/apppointment_detail.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        '''course = self.get_object()
        recipients = message.recipient.all()
        messages = message.message

        if message.enabled is True:
            context_data['enabled'] = 'Активно'
        else:
            context_data['enabled'] = 'Не активно'

        context_data['title'] = f'Название рассылки: {message.name}'
        context_data['text'] = f'{message.description}'
        context_data['creator'] = f'Автор: {message.creator}'
        context_data['recipients'] = recipients
        context_data['object_type'] = 'recipient'
        context_data['message'] = messages
        context_data['post_status'] = message.status
        context_data['period'] = message.period
        context_data['start_at'] = message.start_at
        context_data['next_send_date'] = message.next_send_date'''

        return context_data


class ApppointmentUpdateView(UpdateView):
    model = Apppointment
    form_class = ApppointmentForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.creator = self.request.user

        start_at_str = self.request.POST.get('date')

        if start_at_str:
            start_at = parse_datetime(start_at_str)
            self.object.start_at = make_aware(start_at)
        else:
            form.add_error('date', 'Заполните поле даты и времени.')
            return self.form_invalid(form)

        course = self.request.POST.get('course')

        if not course:
            form.add_error('course', 'Заполните поле курса.')
            return self.form_invalid(form)

        self.object.start_at = make_aware(parse_datetime(self.request.POST['date']))
        self.object.save()
        form.save_m2m()
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        pass

        '''context_data = super().get_context_data(*args, **kwargs)
        context_data['objects_list'] = Post.objects.filter(creator=self.request.user).order_by('-enabled')
        context_data['title'] = f'Список рассылок в базе'
        context_data['object_type'] = 'post
        return context_data'''


class ApppointmentDeleteView(DeleteView):
    model = Apppointment

    def post(self, request, *args, **kwargs):
        # Получаем объект по первичному ключу (pk)
        obj = get_object_or_404(Apppointment, pk=kwargs['pk'])

        # Удаляем объект
        obj.delete()

        # Перенаправляем на нужную страницу после удаления
        return redirect('service:apppointment_form')


class ApppointmentConfirmDeleteView(TemplateView):
    template_name = 'service/apppointment_confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = get_object_or_404(Apppointment, pk=kwargs['pk'])
        return context


class ApppointmentListAdminView(ListView):
    template_name = 'service/apppointment_list.html'

    model = Apppointment

    def get_context_data(self, *args, **kwargs):
        pass
        '''context_data = super().get_context_data(*args, **kwargs)
        from main.services import get_posts_from_cache
        context_data['objects_list'] = get_posts_from_cache()
        context_data['object_type'] = 'post
        return context_data'''


class ServicesCreateView(CreateView):
    model = Services
    form_class = ServicesForm
    success_url = reverse_lazy('service:services_list')
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


class ServicesUpdateView(UpdateView):
    model = Services
    form_class = ServicesForm
    success_url = reverse_lazy('service:services_list')
    def form_valid(self, form):
        self.object = form.save()
        self.object.creator = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        # context_data['objects_list'] = Services.objects.filter(creator=self.request.user).order_by('-enabled')
        context_data['title'] = f'Изменить услугу'
        # context_data['object_type'] = 'message'

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
        context_data['course'] = service.course
        context_data['price'] = service.price
        context_data['top_service'] = service.top_service

        return context_data


class ServicesDeleteView(DeleteView):
    model = Services

    def post(self, request, *args, **kwargs):
        # Получаем объект по первичному ключу (pk)
        obj = get_object_or_404(Services, pk=kwargs['pk'])

        # Удаляем объект
        obj.delete()

        # Перенаправляем на нужную страницу после удаления
        return redirect('service:services_list')


class ServicesConfirmDeleteView(TemplateView):
    template_name = 'service/services_confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = get_object_or_404(Services, pk=kwargs['pk'])
        return context

'''
class ApppointmentListAdminView(ListView):
    template_name = 'service/apppointment_list.html'

    model = Apppointment

    def get_context_data(self, *args, **kwargs):
        pass
     context_data = super().get_context_data(*args, **kwargs)
        from main.services import get_posts_from_cache
        context_data['objects_list'] = get_posts_from_cache()
        context_data['object_type'] = 'post
        return context_data'''



