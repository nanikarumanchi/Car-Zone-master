from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()


def login_user(request):
    next_get = request.GET.get('next')
    next_post = request.POST.get("next")
    _next = next_get or next_post or None
    if request.method == "POST":
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            if _next:
                print("Coming Here")
                return redirect(_next)
            messages.success(
                request, f"{user.username} Logged Successfully into your account.")
            return redirect('accounts_app:dashboard')
        else:
            messages.error(request, "Invalid Login credentials")
    return render(request, 'accounts/login.html', {'next': _next})


def register_user(request):
    if request.method == "POST":
        data = request.POST
        firstname = data.get('firstname')
        lastname = data.get('lastname')
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        if password == confirm_password:
            look_up = Q(username__iexact=username) | Q(email__iexact=email)
            user_qs = User.objects.filter(look_up)
            if user_qs.exists():
                messages.error(request, "User name or Email has already taken")
                return redirect('accounts_app:register')
            else:
                user = User(
                    first_name=firstname, last_name=lastname, email=email, username=username)
                user.set_password(password)
                user.save()
                messages.success(request, "User Successfully created")
                return redirect('accounts_app:login')
        else:
            messages.error(request, "Password's Dosent match")
            return redirect('accounts_app:register')
    return render(request, 'accounts/register.html')


@login_required
def dashboard_user(request):
    user = request.user
    contacts = user.user_enquires.all().order_by('-created_at')
    context = {
        'contacts': contacts,
    }
    return render(request, 'accounts/dashboard.html', context)


@login_required
def logout_user(request):
    auth.logout(request)
    messages.success(request, "You logged out successfully")
    return redirect('accounts_app:login')
