# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Site'
        db.create_table('justdifferent_site', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('domain', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'justdifferentsites', ['Site'])


    def backwards(self, orm):
        # Deleting model 'Site'
        db.delete_table('justdifferent_site')


    models = {
        u'justdifferentsites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'justdifferent_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['justdifferentsites']