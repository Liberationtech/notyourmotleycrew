# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Event.url'
        db.add_column('timelinejs_event', 'url',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'Event.media_outlet'
        db.add_column('timelinejs_event', 'media_outlet',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Event.url'
        db.delete_column('timelinejs_event', 'url')

        # Deleting field 'Event.media_outlet'
        db.delete_column('timelinejs_event', 'media_outlet')


    models = {
        'timelinejs.datetimewithspecificity': {
            'Meta': {'object_name': 'DateTimeWithSpecificity'},
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'datetime_specificity': ('django.db.models.fields.CharField', [], {'default': "'DAY'", 'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'timelinejs.event': {
            'Meta': {'object_name': 'Event'},
            'blockquote': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'credit': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'media': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'media_outlet': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'timeline': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'event'", 'to': "orm['timelinejs.Timeline']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'timelinejs.eventstartdate': {
            'Meta': {'object_name': 'EventStartdate', '_ormbases': ['timelinejs.DateTimeWithSpecificity']},
            'datetimewithspecificity_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['timelinejs.DateTimeWithSpecificity']", 'unique': 'True', 'primary_key': 'True'}),
            'startdate': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'startdate'", 'to': "orm['timelinejs.Event']"})
        },
        'timelinejs.timeline': {
            'Meta': {'object_name': 'Timeline'},
            'blockquote': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'credit': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'media': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'default'", 'max_length': '20'})
        },
        'timelinejs.timelinestartdate': {
            'Meta': {'object_name': 'TimelineStartdate', '_ormbases': ['timelinejs.DateTimeWithSpecificity']},
            'datetimewithspecificity_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['timelinejs.DateTimeWithSpecificity']", 'unique': 'True', 'primary_key': 'True'}),
            'startdate': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'startdate'", 'to': "orm['timelinejs.Timeline']"})
        }
    }

    complete_apps = ['timelinejs']