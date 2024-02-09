from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.utils import IntegrityError
from .models import *

# Create your views here.
def auth_views(request):
    context = {}
    
    # pl_flag = False
    # ff_flag = False
    
    if request.user.is_authenticated:
        context['error'] = 'Ви вже зареєстровані'
    
    if request.method == "POST":
        username = request.POST.get('name')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(username=username,
                                password=password)
            if user:
                login(request, user)
            else:
                context["error"] = "Пароль або логін невірні"
                # pl_flag = True
        else:
            context["error"] = "Заповінть усі поля!"
            # ff_flag = True
    
    # if pl_flag == True:
    #     context["error"] = "Пароль або логін невірні"
    #     print(1)
        
    # if ff_flag == True:
    #     context["error"] = "Заповінть усі поля!"
    #     print(2)

    return render(request, "Add_tenant/authorization.html", context)


def reg_views(request):
    context = {}
    
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        
        if password and name and email and phone:
            if len(password) >= 8:
                try:
                    User.objects.create_user(
                        username=name, 
                        password=password, 
                        email=email)
                except IntegrityError:
                    context["error"] = "Такий користувач вже існує"
            else:
                context["error"] = "Пароль має бути більше або дорівнює 8 символів"
        else:
            context["error"] = "Заповніть усі поля!"
    
    print(context)
                                    
    return render(request, "Add_tenant/registration.html", context)


def add_tenant_views(request):
    context = {}
    
    if request.method == "POST":
        place = request.POST.get('place')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        tenant_name = request.POST.get('tenant_name')
        
        if place and start_date and end_date and tenant_name:
            Tenant.objects.create(
                place = place,
                start_date = start_date,
                end_date = end_date,
                tenant_name = tenant_name,
            )
        else:
            context["error"] = "Поля не заповнені!"
    
    return render(request, "Add_tenant/add_tenant.html", context)