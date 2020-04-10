from datetime import date

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect

from hosApp.models import Hospital, Report, Patient


@login_required(login_url='/login')
def index(request):
    reports = Report.objects.filter(date__exact=date.today())
    context = {
        'active': sum(c.pending for c in reports),
        'death': sum(c.deaths for c in reports),
        'cured': sum(c.discharged for c in reports),
    }
    return render(request, 'home.html', context)


def api(request):
    reports = Report.objects.filter(date__exact=date.today())
    context = {
        'active': sum(c.pending for c in reports),
        'death': sum(c.deaths for c in reports),
        'cured': sum(c.discharged for c in reports),
    }
    return JsonResponse(status=200, data=context)


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect(request.GET.get('next', 'index'))
        return render(request, 'login.html', {'error': 'Invalid Credentials...'})
    return render(request, 'login.html')


@login_required(login_url='/login')
def patient_reg(request):
    if request.method == 'POST':
        Patient.objects.create(
            user=request.user,
            name=request.POST['name'],
            father=request.POST['father'],
            aadhar=request.POST['aadhar'],
            mobile=request.POST['mobile'],
            status=request.POST['status'],
            age=request.POST['age'],
            come_by=request.POST['come_by'],
            gender=request.POST['gender']
        )
    return render(request, 'patient-reg.html')


def register(request):
    if request.method == 'POST':
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        email = request.POST["email"]
        username = request.POST["username"]
        name = request.POST["name"]
        district = request.POST["district"]
        code = request.POST["code"]
        key = request.POST["key"]
        contact = request.POST["contact"]
        address = request.POST["address"]
        type = request.POST["type"]

        if password == confirm_password:
            try:
                User.objects.get(username=username)
                return render(request, 'register.html', {'error': 'Username already exists.'})

            except User.DoesNotExist:
                try:
                    User.objects.create_user(username=username, password=password, email=email)
                    user = auth.authenticate(username=username, password=password)
                    Hospital.objects.create(
                        name=name,
                        user=user,
                        district=district,
                        code=code,
                        key=key,
                        contact=contact,
                        address=address,
                        type=type
                    )
                    auth.login(request, user)
                    return redirect('index')
                except:
                    return render(request, 'register.html', {'error': 'Something Went Wrong!'})

        else:
            return render(request, 'register.html', {'error': 'Password didn\'t match.'})
    return render(request, 'register.html')


@login_required(login_url='/login')
def details(request):
    if request.method == 'POST':
        Report.objects.create(
            user=request.user,
            report=request.FILES['report'],
            sample=request.POST['sample'],
            positive=request.POST['positive'],
            negative=request.POST['negative'],
            pending=request.POST['pending'],
            deaths=request.POST['deaths'],
            discharged=request.POST['discharged'],
        )
    return render(request, 'todays-details.html')


@login_required(login_url='/login')
def logout(request):
    auth.logout(request)
    return redirect('index')
