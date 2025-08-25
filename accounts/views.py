from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.urls import reverse

# -------------------- LOGIN VIEW --------------------
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('menu_list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

# -------------------- SIGNUP VIEW --------------------
def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            token = default_token_generator.make_token(user)
            uid = user.pk
            verify_url = request.build_absolute_uri(
                reverse('verify_email', kwargs={'uid': uid, 'token': token})
            )

            send_mail(
                'Verify your email',
                f'Click this link to verify your account: {verify_url}',
                'noreply@yourdomain.com',
                [user.email],
                fail_silently=False,
            )

            return render(request, 'accounts/check_email.html')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

# -------------------- EMAIL VERIFICATION --------------------
def verify_email(request, uid, token):
    try:
        user = User.objects.get(pk=uid)
    except User.DoesNotExist:
        return render(request, 'accounts/email_invalid.html')

    if default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'accounts/email_verified.html')
    else:
        return render(request, 'accounts/email_invalid.html')

# -------------------- LOGOUT VIEW --------------------
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

# -------------------- PROFILE EDIT VIEW --------------------
@login_required
def profile_edit_view(request):
    user = request.user
    profile = user.profile

    if request.method == "POST":
        user.first_name = request.POST.get("first_name", user.first_name)
        user.last_name = request.POST.get("last_name", user.last_name)
        user.email = request.POST.get("email", user.email)

        if "avatar" in request.FILES:
            profile.avatar = request.FILES["avatar"]

        user.save()
        profile.save()

        return redirect("menu_list")

    return render(request, "accounts/profile_edit.html")
