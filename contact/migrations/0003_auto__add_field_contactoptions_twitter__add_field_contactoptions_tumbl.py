# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ContactOptions.twitter'
        db.add_column(u'contact_contactoptions', 'twitter',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'ContactOptions.tumblr'
        db.add_column(u'contact_contactoptions', 'tumblr',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ContactOptions.twitter'
        db.delete_column(u'contact_contactoptions', 'twitter')

        # Deleting field 'ContactOptions.tumblr'
        db.delete_column(u'contact_contactoptions', 'tumblr')


    models = {
        u'contact.contactoptions': {
            'Meta': {'object_name': 'ContactOptions'},
            'addressline1': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'addressline2': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'backgroundImage': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'contactmessage': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'blank': 'True'}),
            'contactsignoff': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'blank': 'True'}),
            'county': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mapurl': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['sites.Site']", 'unique': 'True'}),
            'tumblr': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['contact']