from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView, TemplateView
import secrets

from service.models import Apppointment
from users.forms import UserRegisterForm, MasseurForm
from users.models import User, Masseur
from config.settings import EMAIL_HOST_USER


class UserCreateView(CreateView):
    login_url = reverse_lazy('users:login')
    model = User

    form_class = UserRegisterForm

    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user = form.save()
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}'
        send_mail(
            subject='Подтверждение почты',
            message=f'Перейдите по ссылке для подтверждения {url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)


def email_verification(token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.token = ''
    user.save()
    return redirect(reverse("users:login"))


class MasseurCreateView(PermissionRequiredMixin, CreateView):
    model = Masseur
    form_class = MasseurForm
    success_url = reverse_lazy('users:masseur_list')
    permission_required = 'create_masseur'

    def form_valid(self, form):
        self.object = form.save()
        self.object.creator = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)
        # context_data['objects_list'] = Services.objects.filter(creator=self.request.user).order_by('-enabled')
        context_data['title'] = f'Добавление массажиста'
        # context_data['object_type'] = 'message'

        return context_data


class MasseurListAdminView(PermissionRequiredMixin, ListView):
    template_name = 'masseur_list.html'
    permission_required = 'view_masseurs'

    model = Masseur

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['objects_list'] = Masseur.objects.all()
        context_data['title'] = f'Наши услуги'
        return context_data


class MasseurUpdateView(PermissionRequiredMixin, UpdateView):
    model = Masseur
    form_class = MasseurForm
    success_url = reverse_lazy('users:masseur_list')
    permission_required = 'change_masseur'

    def form_valid(self, form):
        self.object = form.save()
        self.object.creator = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)
        # context_data['objects_list'] = Services.objects.filter(creator=self.request.user).order_by('-enabled')
        context_data['title'] = f'Изменить услугу'
        # context_data['object_type'] = 'message'

        return context_data


class MasseurDetailView(PermissionRequiredMixin, DetailView):
    model = Masseur
    template_name = 'users/masseur_detail.html'
    permission_required = 'view_masseurs'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        masseur = self.get_object()

        context_data['name'] = masseur.name
        context_data['surname'] = masseur.surname
        context_data['photo'] = masseur.photo
        context_data['description'] = masseur.description
        context_data['phone'] = masseur.phone

        return context_data


class MasseurDeleteView(PermissionRequiredMixin, DeleteView):
    model = Masseur
    permission_required = 'delete_masseur'

    def post(self, request, *args, **kwargs):
        # Получаем объект по первичному ключу (pk)
        obj = get_object_or_404(Masseur, pk=kwargs['pk'])

        # Удаляем объект
        obj.delete()

        # Перенаправляем на нужную страницу после удаления
        return redirect('users:masseur_list')


class MasseurConfirmDeleteView(PermissionRequiredMixin, TemplateView):
    template_name = 'users/masseur_confirm_delete.html'
    permission_required = 'delete_masseur'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = get_object_or_404(Masseur, pk=kwargs['pk'])
        return context


class UserTemplateView(LoginRequiredMixin, TemplateView):
    model = User
    template_name = 'users/user_detail.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        user = self.request.user

        context_data['first_name'] = user.first_name
        context_data['second_name'] = user.second_name
        context_data['avatar'] = user.avatar
        context_data['age'] = user.age
        context_data['email'] = user.email
        context_data['phone'] = user.phone
        context_data['app_service_list'] = Apppointment.objects.filter(creator=self.request.user)

        return context_data
