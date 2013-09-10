from django.shortcuts import render
from django.contrib.sites.models import get_current_site
from models import ContactOptions

def contact(request):
   Site = get_current_site(request)
   contact = ContactOptions.objects.get(site=Site)
   context = {'global_site':Site, "contact" : contact }
   return render(request, 'contact/contact.html', context)
