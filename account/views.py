from django.contrib.auth import get_user_model, login, authenticate,logout
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.contrib import messages
from django.urls import reverse

User = get_user_model()

def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Проверка на пустые поля
        if not username or not email or not password1 or not password2:
            messages.error(request, "Все поля обязательны для заполнения.")
            return render(request, 'account/register.html')

        # Проверка на совпадение паролей
        if password1 != password2:
            messages.error(request, "Пароли не совпадают.")
            return render(request, 'account/register.html')

        # Проверка сложности пароля (можно добавить больше проверок по необходимости)
        if len(password1) < 8:
            messages.error(request, "Пароль должен быть не менее 8 символов.")
            return render(request, 'account/register.html')

        # Создание пользователя
        try:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.is_active = False  # Деактивируем пользователя до активации
            user.save()
        except Exception as e:
            messages.error(request, f"Ошибка при создании пользователя: {e}")
            return render(request, 'account/register.html')

        # Отправка активационного письма
        current_site = get_current_site(request)
        email_subject = 'Подтверждение вашего аккаунта'
        message = render_to_string('account/activation_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        email_message = EmailMessage(email_subject, message, to=[email])

        try:
            email_message.send()
        except Exception as e:
            messages.error(request, f"Ошибка при отправке письма: {e}")
            return render(request, 'account/register.html')

        messages.success(request, "Регистрация прошла успешно! Проверьте свою почту для подтверждения аккаунта.")
        return redirect('login')  # Перенаправление на страницу логина

    return render(request, 'account/register.html')



#Вьюшка активации аккаунта
def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        login(request, user)
        return redirect(reverse('login'))
    else:
        messages.error(request, 'Срок действия ссылки истек или произошла ошибка.')
        return redirect('activation_complete')

#Вьюшка логина
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Используем get вместо прямого доступа
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Перенаправление на главную страницу или другую
        else:
            messages.error(request, 'Неверное имя пользователя или пароль.')

    return render(request, 'account/login.html')



# Страница логаута
def logout_view(request):
    logout(request)
    messages.success(request, 'Вы вышли из системы.')
    return redirect('home')  # Перенаправление на страницу логина

#?
def activation_view(request):
    return render(request, 'account/activation_complete.html')
#?
def activation_complete_view(request):
    return render(request, 'account/active.html')