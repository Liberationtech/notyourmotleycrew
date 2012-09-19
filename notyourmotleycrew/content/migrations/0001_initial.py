# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'NYCMImage'
        db.create_table('content_nycmimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal('content', ['NYCMImage'])


    def backwards(self, orm):
        # Deleting model 'NYCMImage'
        db.delete_table('content_nycmimage')


    models = {
        'content.nycmimage': {
            'Meta': {'object_name': 'NYCMImage'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['content']