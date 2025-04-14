from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    
    #Create a file named forms.py inside the contactform directory.
    #We're creating a ContactForm class that inherits from forms.Form.
    #name, email, and message are the fields of our form.
    #forms.CharField, forms.EmailField, and forms.Textarea are Django's built-in form field types.
    #This makes it so that django handles the creation of the html form, and also handles validation of the form data.