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
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('intro', self.gf('django.db.models.fields.TextField')(max_length=1000, blank=True)),
            ('maintext', self.gf('django.db.models.fields.TextField')(max_length=1000, blank=True)),
            ('outro', self.gf('django.db.models.fields.TextField')(max_length=1000, blank=True)),
            ('backgroundImage', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'about', ['AboutOptions'])


    def backwards(self, orm):
        # Deleting model 'AboutOptions'
        db.delete_table(u'about_aboutoptions')


    models = {
        u'about.aboutoptions': {
            'Meta': {'object_name': 'AboutOptions'},
            'backgroundImage': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intro': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'blank': 'True'}),
            'maintext': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'outro': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"})
        },
        u'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['about']