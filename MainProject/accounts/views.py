# Test your GPT code here's
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import View
from django.core.mail import send_mail
from django.conf import settings
from .forms import (
    CreateUserForm,
    UserRegistrationForm,
    CustomerRegistrationForm,
    AddressForm,
    ForgetPasswordForm,
    OTPForm,
    ResetPasswordForm,
)
import random

# About view
def about(request):
    return render(request, "About.html")

# Registration view
# def register_view(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        email = request.POST.get("email")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        pass1 = request.POST.get("pass1")
        cpass = request.POST.get("pass2")
        dob = request.POST.get("dob")

        if pass1 != cpass:
            messages.warning(request, "Passwords do not match!")
            return redirect("register")

        if User.objects.filter(username=uname).exists():
            messages.info(request, "Username is already registered!")
            return redirect("register") 
        
        if User.objects.filter(email=email).exists():
            messages.info(request, "Username is already registered!")
            return redirect("register")

        myuser = User.objects.create_user(username=uname, email=email, password=pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        messages.success(request, "Registration successful! Please log in.")
        return redirect("login")
    elif request.method=="GET":
        cform = CustomerRegistrationForm()
        uform = CreateUserForm()
        return render(request, "account/mysignup.html",{'cform':cform,'uform':uform})
    return render(request, "signup.html")
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import CustomerRegistrationForm, CreateUserForm
from .models import Customer

def register_view(request):
    if request.method == "POST":
        uform = CreateUserForm(request.POST)
        cform = CustomerRegistrationForm(request.POST)

        if uform.is_valid() and cform.is_valid():
            # Save the User form
            user = uform.save(commit=False)  # Create user instance without saving immediately
            user.set_password(uform.cleaned_data['password1'])  # Ensure the password is hashed
            user.save()

            # Save the Customer form and link it to the User
            customer = cform.save(commit=False)
            customer.user = user
            customer.save()

            # Provide success message and redirect
            messages.success(request, 'Your account has been created successfully. Please log in.')
            return redirect('login')
        else:
            # Display errors if any
            messages.error(request, 'There were errors in the form. Please correct them.')

    else:
        # For GET request, render blank forms
        uform = CreateUserForm()
        cform = CustomerRegistrationForm()

    return render(request, "account/mysignup.html", {'uform': uform, 'cform': cform})

# Login view
def login_view(request):
    if request.method == "POST":
        user = request.POST.get("username")
        pass1 = request.POST.get("pass1")
        myuser = authenticate(username=user, password=pass1)

        if myuser is not None:
            login(request, myuser)
            messages.success(request, "Login successful!")
            return redirect("/")
        else:
            messages.error(request, "Invalid email or password.")
            return redirect("login")

    return render(request, "login.html")

# Logout view
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("login")

# Forgot Password view
class ForgotPassword(View):
    def get(self, request):
        context = {"form": ForgetPasswordForm()}
        return render(request, "account/form.html", context)

    def post(self, request):
        form = ForgetPasswordForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]

            try:
                user = User.objects.get(username=username, email=email)
                otp = random.randint(1000, 9999)
                send_otp_to_email(user, otp)
                request.session["otp"] = otp
                request.session["username"] = username
                messages.success(request, "OTP sent to your email!")
                print("here i am",otp)
                return render(
                    request,
                    "account/form.html",
                    {"form": OTPForm(), "form_action": "/accounts/verify-otp/"},
                )
            except User.DoesNotExist:
                messages.error(request, "No user found with this username and email.")
                return redirect("forgot_password")

        messages.error(request, "Invalid form submission.")
        return redirect("forgot_password")

# Helper function to send OTP
def send_otp_to_email(user, otp):
    try:
        send_mail(
            subject="OTP for Reset Password",
            message=f"{otp} is your OTP for password reset.",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
            fail_silently=False,
        )
        print(f"OTP: {otp}")  # Debugging; remove in production
    except Exception as e:
        print(f"Error sending email: {e}")

# OTP Verification view
def verify_otp(request):
    if request.method == "POST":
        otp = request.session.get("otp")
        username = request.session.get("username")
        entered_otp = request.POST.get("otp")

        if entered_otp and otp and int(entered_otp) == int(otp):
            return render(
                request,
                "account/form.html",
                {"form": ResetPasswordForm(), "form_action": "/accounts/reset-password/"},
            )
        else:
            messages.error(request, "Invalid OTP.")
            return render(
                request,
                "account/form.html",
                {"form": OTPForm(), "form_action": "/accounts/verify-otp/"},
            )

    return redirect("Home")

# Reset Password view
def reset_password(request):
    if request.method == "POST":
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        username = request.session.get("username")

        if password == confirm_password:
            user = get_object_or_404(User, username=username)
            user.set_password(password)
            user.save()

            send_mail(
                subject="Password Reset Successful",
                message="Your password has been reset successfully.",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email],
                fail_silently=True,
            )

            del request.session["username"]
            del request.session["otp"]

            messages.success(request, "Password reset successful. Please log in.")
            return redirect("login")
        else:
            messages.error(request, "Passwords do not match.")
            return render(
                request,
                "account/form.html",
                {"form": ResetPasswordForm(), "form_action": "/account/reset-password/"},
            )

    return redirect("home")


