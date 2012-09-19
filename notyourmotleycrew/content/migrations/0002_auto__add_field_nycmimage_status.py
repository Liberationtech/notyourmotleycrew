# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'NYCMImage.status'
        db.add_column('content_nycmimage', 'status',
                      self.gf('django.db.models.fields.CharField')(default='NOTCHECKED', max_length=30),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'NYCMImage.status'
        db.delete_column('content_nycmimage', 'status')


    models = {
        'content.nycmimage': {
            'Meta': {'object_name': 'NYCMImage'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'NOTCHECKED'", 'max_length': '30'})
        }
    }

    complete_apps = ['content']