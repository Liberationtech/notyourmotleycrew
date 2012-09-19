# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'NYCMImage'
        db.delete_table('content_nycmimage')

        # Adding model 'NYMCImage'
        db.create_table('content_nymcimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('status', self.gf('django.db.models.fields.CharField')(default='NOTCHECKED', max_length=30)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('content', ['NYMCImage'])


    def backwards(self, orm):
        # Adding model 'NYCMImage'
        db.create_table('content_nycmimage', (
            ('status', self.gf('django.db.models.fields.CharField')(default='NOTCHECKED', max_length=30)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal('content', ['NYCMImage'])

        # Deleting model 'NYMCImage'
        db.delete_table('content_nymcimage')


    models = {
        'content.nymcimage': {
            'Meta': {'object_name': 'NYMCImage'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'NOTCHECKED'", 'max_length': '30'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'})
        }
    }

    complete_apps = ['content']