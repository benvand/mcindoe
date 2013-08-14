# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Post'
        db.create_table(u'blog_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('created', self.gf('django.db.models.fields.TimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.TimeField')(auto_now=True, blank=True)),
            ('userid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['justdifferent.IQUser'])),
        ))
        db.send_create_signal(u'blog', ['Post'])

        # Adding model 'Comment'
        db.create_table(u'blog_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('created', self.gf('django.db.models.fields.TimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.TimeField')(auto_now=True, blank=True)),
            ('userid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['justdifferent.IQUser'])),
            ('postid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blog.Post'])),
        ))
        db.send_create_signal(u'blog', ['Comment'])


    def backwards(self, orm):
        # Deleting model 'Post'
        db.delete_table(u'blog_post')

        # Deleting model 'Comment'
        db.delete_table(u'blog_comment')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'blog.comment': {
            'Meta': {'ordering': "('created',)", 'object_name': 'Comment'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.TimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.TimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'postid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blog.Post']"}),
            'userid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['justdifferent.IQUser']"})
        },
        u'blog.post': {
            'Meta': {'ordering': "('created',)", 'object_name': 'Post'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.TimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.TimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'userid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['justdifferent.IQUser']"})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'justdifferent.iquser': {
            'Meta': {'object_name': 'IQUser'},
            'avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'mailing': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'password_hint': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'password_hint_response': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'signoff': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user_occupation': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        }
    }

    complete_apps = ['blog']