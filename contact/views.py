# Create your views here.
#Below imports negated by render shortcut method
#from django.http import HttpResponse
#from django.template import RequestContext, loader
from django.shortcuts import render
from contact.models import ContactOptions
from django.conf import settings
SiteName = settings.SITE_NAME
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
    #context = {'contact_details': ContactOptions,'site_name': SiteName}
    context = {'site_name': SiteName}
    return render(request, 'contact/comingsoon.html', context)
