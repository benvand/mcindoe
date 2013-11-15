from django.shortcuts import render
from django.contrib.sites.models import get_current_site
from models import ContactOptions

def contact(request):
    site = get_current_site(request)
    contact = ContactOptions.objects.get(site=site)
    context = {'global_site':site, "contact" : contact }
    return render(request, 'contact/contact.html', context)
