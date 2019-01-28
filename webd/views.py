from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import Form,Check
from .models import FormM
from django.views import generic

def main(request):

    if request.method=='POST':
        form = Form(request.POST)
        if form.is_valid():
            print("Valid")
            form.save()
            email=form.cleaned_data['email']
            subject="Thanks you for Appling TDC Internship"
            from_mail=settings.EMAIL_HOST_USER
            to_email=[email]
            message="""Successfully Submited"""
            #send_mail(subject=subject,from_email=from_mail,recipient_list=to_email,message=message,fail_silently=False)


    form = Form()
    return render(request,'webd/home.html',{'form':form})

class IndexViewPro(generic.ListView):
    template_name = 'webd/name.html'
    context_object_name = 'form'

    def get_queryset(self):
        return FormM.objects.all()

    def post(self,request):

        if request.method == 'POST':
            checked = Check(request.POST)
            if checked.is_valid():
                email = request.POST.getlist('check')
                subject= checked.cleaned_data['subject']
                message = checked.cleaned_data['message']
                print(email)
                print(subject)
                print(message)
                subject = subject
                from_mail = settings.EMAIL_HOST_USER
                message = message
                #send_mail(subject=subject,from_email=from_mail,recipient_list=email,message=message,fail_silently=False)

        checked = Check()
        return render(request, 'webd/name.html', {'checked': checked})



