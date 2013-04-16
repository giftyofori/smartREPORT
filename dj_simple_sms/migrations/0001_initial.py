# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SMS'
        db.create_table('dj_simple_sms_sms', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('to_number', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('from_number', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('body', self.gf('django.db.models.fields.CharField')(max_length=160)),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('dj_simple_sms', ['SMS'])

        # Adding model 'Device'
        db.create_table('dj_simple_sms_device', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('key', self.gf('django.db.models.fields.CharField')(default='c89b03487bdd4683884e1b426cc51a1d', max_length=32, db_index=True)),
        ))
        db.send_create_signal('dj_simple_sms', ['Device'])


    def backwards(self, orm):
        # Deleting model 'SMS'
        db.delete_table('dj_simple_sms_sms')

        # Deleting model 'Device'
        db.delete_table('dj_simple_sms_device')


    models = {
        'dj_simple_sms.device': {
            'Meta': {'object_name': 'Device'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'default': "'486dc9917868428f90e76ff2971dd63e'", 'max_length': '32', 'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'dj_simple_sms.sms': {
            'Meta': {'object_name': 'SMS'},
            'body': ('django.db.models.fields.CharField', [], {'max_length': '160'}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'from_number': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'to_number': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['dj_simple_sms']