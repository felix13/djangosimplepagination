from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.conf import settings


from uploads.models import Document
from uploads.forms import DocumentForm


def home(request):

    documents = Document.objects.all()
     
    paginator = Paginator(documents, 2) # Show 2 documents per page.

    page_number = request.GET.get('page')
    
    page_obj = paginator.get_page(page_number) # If the page isn’t a number, it returns the first page.
    
    return render(request, 'uploads/home.html', { 'page_obj' : page_obj })




def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'uploads/model_form_upload.html', {
        'form': form
    })
