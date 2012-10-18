# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'NYMCImage.email'
        db.add_column('content_nymcimage', 'email',
                      self.gf('django.db.models.fields.EmailField')(default='example@example.com', max_length=75),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'NYMCImage.email'
        db.delete_column('content_nymcimage', 'email')


    models = {
        'content.nymcimage': {
            'Meta': {'object_name': 'NYMCImage'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'email': ('django.db.models.fields.EmailField', [], {'default': "'example@example.com'", 'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'image1000': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'image200': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'image400': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'image600': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'image800': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
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