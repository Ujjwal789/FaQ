from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import FAQ
from django.http import HttpResponse
from .forms import FAQForm  # Make sure you're using one form class

def faq_list(request):
    faqs = FAQ.objects.all().values()  
    return JsonResponse(list(faqs), safe=False)  

def homepage(request):
    return render(request, "faqs/home.html")  

def faq_page(request):
    faqs = [
        {"question": "What is BTU Page?", "answer": "BTU Page is a medical chat application."},
        {"question": "How can I reset my password?", "answer": "Go to settings and click 'Reset Password'."}
    ]
    return render(request, "faqs/page.html", {"faqs": faqs})

def submit_faq(request):
    if request.method == "POST":
        form = FAQForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('faq-success')  
    else:
        form = FAQForm()
    return render(request, 'submit_faq.html', {'form': form})

 # Render the submit FAQ page
def faq_success(request):
    return render(request, "faqs/success.html")