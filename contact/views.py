# Create your views here.
#Below imports negated by render shortcut method
#from django.http import HttpResponse
#from django.template import RequestContext, loader
from django.shortcuts import render
from contact.models import ContactOptions
from django.conf import settings
from django.contrib.sites.models import get_current_site

#SiteName = settings.SITE_NAME
#ContactOptions = ContactOptions.objects.all()[0]
# def comingSoon(request):
#     template = loader.get_template('contact/comingsoon.html')
#     context = RequestContext(request, {
#         'contact_details': ContactOptions,
#     })
#     return HttpResponse(template.render(context))


# def comingSoon(request):
#     return HttpResponse("Hello, world. You're at the Coming Soon page")

def comingSoon(request):
    Site = get_current_site(request)
    context = {'global_site':Site,}
    print Site, context
    #context = {'site_name': repr(Site)}
    return render(request, 'contact/comingsoon.html', context)
