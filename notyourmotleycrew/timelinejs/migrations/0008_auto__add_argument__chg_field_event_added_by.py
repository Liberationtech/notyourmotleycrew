# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Argument'
        db.create_table('timelinejs_argument', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('body', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('timelinejs', ['Argument'])

        # Adding M2M table for field arguments on 'Event'
        db.create_table('timelinejs_event_arguments', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm['timelinejs.event'], null=False)),
            ('argument', models.ForeignKey(orm['timelinejs.argument'], null=False))
        ))
        db.create_unique('timelinejs_event_arguments', ['event_id', 'argument_id'])


        # Changing field 'Event.added_by'
        db.alter_column('timelinejs_event', 'added_by_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['auth.User']))

    def backwards(self, orm):
        # Deleting model 'Argument'
        db.delete_table('timelinejs_argument')

        # Removing M2M table for field arguments on 'Event'
        db.delete_table('timelinejs_event_arguments')


        # User chose to not deal with backwards NULL issues for 'Event.added_by'
        raise RuntimeError("Cannot reverse this migration. 'Event.added_by' and its values cannot be restored.")

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'timelinejs.argument': {
            'Meta': {'object_name': 'Argument'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'timelinejs.datetimewithspecificity': {
            'Meta': {'object_name': 'DateTimeWithSpecificity'},
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'datetime_specificity': ('django.db.models.fields.CharField', [], {'default': "'DAY'", 'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'timelinejs.event': {
            'Meta': {'object_name': 'Event'},
            'added_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'event'", 'null': 'True', 'to': "orm['auth.User']"}),
            'arguments': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['timelinejs.Argument']", 'symmetrical': 'False'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'blockquote': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'cleared_for_publication': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'credit': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'facebook_total_count': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
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