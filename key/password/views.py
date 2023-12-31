from django.shortcuts import render, redirect
from django.http import HttpResponse
from .utils import request_validator, password_generator
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Password
from .forms import CreateUserForm, AddPasswordForm, GeneratePasswordForm
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

@login_required(login_url='login')
def index(request):
    user_passwords = Password.objects.filter(user=request.user).order_by('name')
    generated_password = request.session.get('generated_password', None)
    if 'submit_password' in request.POST:
        add_password_form = AddPasswordForm(request.POST, initial={'password': generated_password})
    else:
        add_password_form = AddPasswordForm(initial={'password': generated_password})
    generate_password_form = GeneratePasswordForm(request.POST or None)

    if request.method == 'POST':
        if 'generate_password' in request.POST:
            if generate_password_form.is_valid():
                password_request = {
                    'human': generate_password_form.cleaned_data['human'],
                    'length': generate_password_form.cleaned_data['length'],
                    'div': generate_password_form.cleaned_data['div'],
                    'caps': generate_password_form.cleaned_data['caps'],
                    'nums': generate_password_form.cleaned_data['nums'],
                    'valid': None
                }
                logger.info('Password request: %s', password_request)
                request_validator(password_request)
                generated_password = password_generator(password_request)
                request.session['generated_password'] = generated_password
            else:
                logger.error('GeneratePasswordForm errors: %s', generate_password_form.errors)
                logger.info('GeneratePasswordForm POST data: %s', request.POST)

        elif 'submit_password' in request.POST:
            if add_password_form.is_valid():
                name = add_password_form.cleaned_data['name']
                url = add_password_form.cleaned_data['url']
                username = add_password_form.cleaned_data['username']
                ciphertext = add_password_form.cleaned_data['password']
                tags = add_password_form.cleaned_data['tags']
                comment = add_password_form.cleaned_data['comment']
                entry = Password(user=request.user, name=name, url=url, username=username, ciphertext=ciphertext, tags=tags, comment=comment)
                entry.save()
                generated_password = None
            else:
                logger.error('AddPasswordForm errors: %s', add_password_form.errors)
                logger.info('AddPasswordForm POST data: %s', request.POST)

    return render(request, "password/index.html", {
        "user_passwords": user_passwords,
        "generated_password": generated_password,
        "add_password_form": add_password_form,
        "generate_password_form": generate_password_form,
    })

'''This view is handling 'get_password' requests from the index.html template.
The get_password function takes in a request object and a password_id as an argument.
It fetches the password object from the database using its password_id. If the current user
matches the user that created the password, the password is returned as a string. 
If not, a 403 error is returned.'''

@login_required(login_url='login')
def get_password(request, password_id):
    password = Password.objects.get(id=password_id)
    if password.user == request.user:
        return HttpResponse(password.ciphertext)
    else:
        return HttpResponse(status=403)

@login_required(login_url='login')
def delete_password(request, password_id):
    password = Password.objects.get(id=password_id)
    if password.user == request.user:
        password.delete()
        return redirect('password')
    else:
        return HttpResponse(status=403)

def login_page(request):  
    if request.user.is_authenticated: # If out user is logged in, redirect them to index.
        return redirect('password')
    else:
        if request.method == 'POST': 
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None: 
                login(request, user)
                return redirect('password')
            else:
                messages.info(request, 'Username or password is incorrect.')

        return render(request, "password/login.html")


# Log user out. Redirect to 'login'.
def logout_user(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.user.is_authenticated: # If out user is logged in, redicet them to 'password'.
        return redirect('password')
    else:
        reg_form = CreateUserForm() # Get an object of out custom class.
        if request.method == 'POST':
            reg_form = CreateUserForm(request.POST) # Store POST data in our form.
            if reg_form.is_valid(): # Validate the form.
                reg_form.save() # Save the form, crateing the user.
                user = reg_form.cleaned_data.get('username') # Get the username, pass that with a message for feedback.
                messages.success(request, 'Account was created ' + user)
                return redirect('login')

        # Sending our reg_form to be filled out.
        return render(request, "password/register.html", {
            "reg_form": reg_form
        })

def about(request):
    return render(request, "password/about.html")