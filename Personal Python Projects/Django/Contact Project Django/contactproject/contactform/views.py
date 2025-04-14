from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data (e.g., send an email)
            # ...
            return redirect('success')  # Redirect to success page
    else:
        form = ContactForm()
    return render(request, 'contactform/contact_form.html', {'form': form})

def success(request):
    return render(request, 'contactform/success.html')

#contact_form handles both GET and POST requests.
#If it's a POST request (form submission), it validates the form data.
#form.cleaned_data contains the validated data.
#send_mail sends an email with the form data.
#redirect('success') redirects to the success view after successful submission.
#If it's a GET request, it creates an empty form.
#The view passes the form to the template.
#The success view just renders a simple success page.
#Note that you will need to setup your email settings in settings.py for the emails to be sent.