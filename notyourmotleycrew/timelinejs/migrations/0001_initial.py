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
            ('startdate', self.gf('django.db.models.fields.DateTimeField')()),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('media', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('blockquote', self.gf('django.db.models.fields.TextField')()),
            ('credit', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=400)),
        ))
        db.send_create_signal('timelinejs', ['Timeline'])

        # Adding model 'Event'
        db.create_table('timelinejs_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('startdate', self.gf('django.db.models.fields.DateTimeField')()),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('media', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('blockquote', self.gf('django.db.models.fields.TextField')()),
            ('credit', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('timeline', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['timelinejs.Timeline'])),
        ))
        db.send_create_signal('timelinejs', ['Event'])


    def backwards(self, orm):
        # Deleting model 'Timeline'
        db.delete_table('timelinejs_timeline')

        # Deleting model 'Event'
        db.delete_table('timelinejs_event')


    models = {
        'timelinejs.event': {
            'Meta': {'object_name': 'Event'},
            'blockquote': ('django.db.models.fields.TextField', [], {}),
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'credit': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'media': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'startdate': ('django.db.models.fields.DateTimeField', [], {}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'timeline': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['timelinejs.Timeline']"})
        },
        'timelinejs.timeline': {
            'Meta': {'object_name': 'Timeline'},
            'blockquote': ('django.db.models.fields.TextField', [], {}),
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'credit': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'media': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'startdate': ('django.db.models.fields.DateTimeField', [], {}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'default'", 'max_length': '20'})
        }
    }

    complete_apps = ['timelinejs']