# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ContactOptions'
        db.create_table(u'contact_contactoptions', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['sites.Site'], unique=True)),
            ('contactmessage', self.gf('django.db.models.fields.TextField')(max_length=1000, blank=True)),
            ('addressline1', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('addressline2', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('county', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('postcode', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('mapurl', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('contactsignoff', self.gf('django.db.models.fields.TextField')(max_length=1000, blank=True)),
            ('backgroundImage', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'contact', ['ContactOptions'])


    def backwards(self, orm):
        # Deleting model 'ContactOptions'
        db.delete_table(u'contact_contactoptions')


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
            'site': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['sites.Site']", 'unique': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'backgroundImage1': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'backgroundImage2': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'favicon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tumblr': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['contact']