from django.contrib.sites.admin import SiteAdmin
from models import newVariables


SiteAdmin.list_display = SiteAdmin.list_display + tuple([i[0] for i in newVariables])
