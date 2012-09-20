# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'NYMCImage.image200'
        db.add_column('content_nymcimage', 'image200',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'NYMCImage.image200'
        db.delete_column('content_nymcimage', 'image200')


    models = {
        'content.nymcimage': {
            'Meta': {'object_name': 'NYMCImage'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'image200': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'NOTCHECKED'", 'max_length': '30'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'})
        },
        'content.sign': {
            'Meta': {'object_name': 'Sign'},
            'authorized': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'})
        }
    }

    complete_apps = ['content']