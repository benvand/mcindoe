# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AboutOptions'
        db.create_table(u'about_aboutoptions', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['sites.Site'], unique=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('intro', self.gf('django.db.models.fields.TextField')(max_length=1000, blank=True)),
            ('maintext', self.gf('django.db.models.fields.TextField')(max_length=1000, blank=True)),
            ('outro', self.gf('django.db.models.fields.TextField')(max_length=1000, blank=True)),
            ('backgroundImage', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'about', ['AboutOptions'])


    def backwards(self, orm):
        # Deleting model 'AboutOptions'
        db.delete_table(u'about_aboutoptions')


    models = {
        u'about.aboutoptions': {
            'Meta': {'object_name': 'AboutOptions'},
            'backgroundImage': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intro': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'blank': 'True'}),
            'maintext': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'blank': 'True'}),
            'outro': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['sites.Site']", 'unique': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'backgroundImage1': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'backgroundImage2': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'favicon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tumblr': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['about']