from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def sendemail(request):
    if request.method == "POST":  # ✅ Send email only on POST request
        send_mail(
            "Subject here",
            "Here is the message.",
            settings.EMAIL_HOST_USER,  # ✅ Uses settings.py configuration
            ["recipient@example.com"],  # ✅ Replace with actual recipient email
            fail_silently=False,
        )
        return render(request, 'email.html', {"message": "Email sent successfully!"})

    return render(request, 'email.html')  # Renders form if GET request
