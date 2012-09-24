# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Timeline'
        db.create_table('timelinejs_timeline', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('type', self.gf('django.db.models.fields.CharField')(default='default', max_length=20)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('media', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('blockquote', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('credit', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
        ))
        db.send_create_signal('timelinejs', ['Timeline'])

        # Adding model 'DateTimeWithSpecificity'
        db.create_table('timelinejs_datetimewithspecificity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('datetime_specificity', self.gf('django.db.models.fields.CharField')(default='DAY', max_length=30)),
        ))
        db.send_create_signal('timelinejs', ['DateTimeWithSpecificity'])

        # Adding model 'TimelineStartdate'
        db.create_table('timelinejs_timelinestartdate', (
            ('datetimewithspecificity_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['timelinejs.DateTimeWithSpecificity'], unique=True, primary_key=True)),
            ('startdate', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['timelinejs.Timeline'])),
        ))
        db.send_create_signal('timelinejs', ['TimelineStartdate'])

        # Adding model 'Event'
        db.create_table('timelinejs_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('startdate', self.gf('django.db.models.fields.DateTimeField')()),
            ('startdate_specificity', self.gf('django.db.models.fields.CharField')(default='DAY', max_length=30)),
            ('text', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('media', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('blockquote', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('credit', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True)),
            ('timeline', self.gf('django.db.models.fields.related.ForeignKey')(related_name='event', to=orm['timelinejs.Timeline'])),
        ))
        db.send_create_signal('timelinejs', ['Event'])


    def backwards(self, orm):
        # Deleting model 'Timeline'
        db.delete_table('timelinejs_timeline')

        # Deleting model 'DateTimeWithSpecificity'
        db.delete_table('timelinejs_datetimewithspecificity')

        # Deleting model 'TimelineStartdate'
        db.delete_table('timelinejs_timelinestartdate')

        # Deleting model 'Event'
        db.delete_table('timelinejs_event')


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
            'startdate': ('django.db.models.fields.DateTimeField', [], {}),
            'startdate_specificity': ('django.db.models.fields.CharField', [], {'default': "'DAY'", 'max_length': '30'}),
            'text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'timeline': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'event'", 'to': "orm['timelinejs.Timeline']"})
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