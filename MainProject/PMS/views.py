from django.core.mail import send_mail
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from accounts.models import Customer
from django.core.validators import validate_email
from django.conf import settings


User = get_user_model()

def contact(request):
    if request.method == 'POST':
        c_fname = request.POST.get('c_fname')
        c_lname = request.POST.get('c_lname')
        c_subject = request.POST.get('c_subject', 'No Subject')
        c_message = request.POST.get('c_message', '')

        # Get email based on login status
        if request.user.is_authenticated:
            try:
                customer = Customer.objects.get(user=request.user)
                c_email = request.user.email
            except Customer.DoesNotExist:
                messages.error(request, "Customer profile not found.")
                return redirect('contact')
        else:
            c_email = request.POST.get('c_email')
            try:
                validate_email(c_email)
            except ValidationError:
                messages.error(request, "Invalid email address.")
                return redirect('contact')

        subject = f"{c_subject} - From {c_fname} {c_lname}"
        message = f"Message from {c_fname} {c_lname} ({c_email}):\n\n{c_message}"
        sender = 'your_email@gmail.com'
        recipient = settings.EMAIL_HOST_USER

        try:
            send_mail(subject, message, sender, [recipient])
            messages.success(request, "Thank You for getting in touch.")
        except Exception as e:
            messages.error(request, f"Failed to send your message: {e}")

        return redirect('contact')

    return render(request, 'contact.html', {'user_authenticated': request.user.is_authenticated})
