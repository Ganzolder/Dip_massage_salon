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


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.token = ''
    user.save()
    return redirect(reverse("users:login"))


class MasseurCreateView(CreateView):
    model = Masseur
    form_class = MasseurForm
    success_url = reverse_lazy('users:masseur_list')
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


class MasseurListAdminView(ListView):
    template_name = 'masseur_list.html'

    model = Masseur

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['objects_list'] = Masseur.objects.all()
        context_data['title'] = f'Наши услуги'
        return context_data


class MasseurUpdateView(UpdateView):
    model = Masseur
    form_class = MasseurForm
    success_url = reverse_lazy('users:masseur_list')
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


class MasseurDetailView(DetailView):
    model = Masseur
    template_name = 'users/masseur_detail.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        masseur = self.get_object()

        context_data['name'] = masseur.name
        context_data['surname'] = masseur.surname
        context_data['photo'] = masseur.photo
        context_data['description'] = masseur.description
        context_data['phone'] = masseur.phone



        return context_data


class MasseurDeleteView(DeleteView):
    model = Masseur

    def post(self, request, *args, **kwargs):
        # Получаем объект по первичному ключу (pk)
        obj = get_object_or_404(Masseur, pk=kwargs['pk'])

        # Удаляем объект
        obj.delete()

        # Перенаправляем на нужную страницу после удаления
        return redirect('users:masseur_list')


class MasseurConfirmDeleteView(TemplateView):
    template_name = 'users/masseur_confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = get_object_or_404(Masseur, pk=kwargs['pk'])
        return context


class UserTemplateView(TemplateView):
    model = User
    template_name = 'users/user_detail.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        User = self.request.user

        context_data['first_name'] = User.first_name
        context_data['second_name'] = User.second_name
        context_data['avatar'] = User.avatar
        context_data['age'] = User.age
        context_data['email'] = User.email
        context_data['phone'] = User.phone
        context_data['app_service_list'] = Apppointment.objects.filter(creator=self.request.user)

        return context_data


