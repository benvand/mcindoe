# Create your views here.
#Below imports negated by render shortcut method
#from django.http import HttpResponse
#from django.template import RequestContext, loader
from django.shortcuts import render
from contact.models import ContactOptions


# def comingSoon(request):
#     template = loader.get_template('contact/comingsoon.html')
#     context = RequestContext(request, {
#         'contact_details': ContactOptions,
#     })
#     return HttpResponse(template.render(context))


# def comingSoon(request):
#     return HttpResponse("Hello, world. You're at the Coming Soon page")

def comingSoon(request):
    context = {'contact_details': ContactOptions,}
    return render(request, 'contact/comingsoon.html', context)
