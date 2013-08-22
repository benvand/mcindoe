# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'AboutOptions.site'
        db.alter_column(u'about_aboutoptions', 'site_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['sites.Site'], unique=True))
        # Adding unique constraint on 'AboutOptions', fields ['site']
        db.create_unique(u'about_aboutoptions', ['site_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'AboutOptions', fields ['site']
        db.delete_unique(u'about_aboutoptions', ['site_id'])


        # Changing field 'AboutOptions.site'
        db.alter_column(u'about_aboutoptions', 'site_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site']))

    models = {
        u'about.aboutoptions': {
            'Meta': {'object_name': 'AboutOptions'},
            'backgroundImage': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intro': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'blank': 'True'}),
            'maintext': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'outro': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['sites.Site']", 'unique': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['about']