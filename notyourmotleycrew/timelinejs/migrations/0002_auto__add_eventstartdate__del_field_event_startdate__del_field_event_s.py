# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'EventStartdate'
        db.create_table('timelinejs_eventstartdate', (
            ('datetimewithspecificity_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['timelinejs.DateTimeWithSpecificity'], unique=True, primary_key=True)),
            ('startdate', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['timelinejs.Event'])),
        ))
        db.send_create_signal('timelinejs', ['EventStartdate'])

        # Deleting field 'Event.startdate'
        db.delete_column('timelinejs_event', 'startdate')

        # Deleting field 'Event.startdate_specificity'
        db.delete_column('timelinejs_event', 'startdate_specificity')


    def backwards(self, orm):
        # Deleting model 'EventStartdate'
        db.delete_table('timelinejs_eventstartdate')

        # Adding field 'Event.startdate'
        db.add_column('timelinejs_event', 'startdate',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 9, 24, 0, 0)),
                      keep_default=False)

        # Adding field 'Event.startdate_specificity'
        db.add_column('timelinejs_event', 'startdate_specificity',
                      self.gf('django.db.models.fields.CharField')(default='DAY', max_length=30),
                      keep_default=False)


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
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'media': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'timeline': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'event'", 'to': "orm['timelinejs.Timeline']"})
        },
        'timelinejs.eventstartdate': {
            'Meta': {'object_name': 'EventStartdate', '_ormbases': ['timelinejs.DateTimeWithSpecificity']},
            'datetimewithspecificity_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['timelinejs.DateTimeWithSpecificity']", 'unique': 'True', 'primary_key': 'True'}),
            'startdate': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['timelinejs.Event']"})
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
            'startdate': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['timelinejs.Timeline']"})
        }
    }

    complete_apps = ['timelinejs']