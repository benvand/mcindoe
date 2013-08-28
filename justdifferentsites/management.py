"""
Creates the default Site object.
"""

from django.db.models import signals
from django.db import connections
from django.db import router
from justdifferentsites.models import Site
from justdifferentsites import models as site_app
from django.core.management.color import no_style
from django.conf import settings
ALLOWED_HOSTS
SITE_NAME

def getDomain_Name():
    test = hasattr(settings,'ALLOWED_HOSTS'), hasattr(settings,'SITE_NAME')
    return {'domain':settings.ALLOWED_HOSTS if test[0] else "example.com",
            'name':settings.SITE_NAME if test[1] else "example.com"}


def create_default_site(app, created_models, verbosity, db, **kwargs):
    # Only create the default sites in databases where Django created the table
    if Site in created_models and router.allow_syncdb(db, Site) :
        # The default settings set SITE_ID = 1, and some tests in Django's test
        # suite rely on this value. However, if database sequences are reused
        # (e.g. in the test suite after flush/syncdb), it isn't guaranteed that
        # the next id will be 1, so we coerce it. See #15573 and #16353. This
        # can also crop up outside of tests - see #15346.
        if verbosity >= 2:
            print("Creating Initial Site object")
        siteObjectDefaults = getDomain_Name()
        Site(pk=1, domain=siteObjectDefaults['domain'], name=siteObjectDefaults['name']).save(using=db)

        # We set an explicit pk instead of relying on auto-incrementation,
        # so we need to reset the database sequence. See #17415.
        sequence_sql = connections[db].ops.sequence_reset_sql(no_style(), [Site])
        if sequence_sql:
            if verbosity >= 2:
                print("Resetting sequence")
            cursor = connections[db].cursor()
            for command in sequence_sql:
                cursor.execute(command)

    Site.objects.clear_cache()

signals.post_syncdb.connect(create_default_site, sender=site_app)