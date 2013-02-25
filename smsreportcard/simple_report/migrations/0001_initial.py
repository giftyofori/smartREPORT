# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Report'
        db.create_table('simple_report_report', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('course', self.gf('django.db.models.fields.CharField')(default='BUSINESS', max_length=20)),
            ('phone', self.gf('django.db.models.fields.IntegerField')(default='0243637783', max_length=10)),
        ))
        db.send_create_signal('simple_report', ['Report'])

        # Adding model 'Subject'
        db.create_table('simple_report_subject', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('grade', self.gf('django.db.models.fields.CharField')(default='A', max_length=1)),
            ('report', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['simple_report.Report'])),
        ))
        db.send_create_signal('simple_report', ['Subject'])

        # Adding model 'Subjects'
        db.create_table('simple_report_subjects', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('simple_report', ['Subjects'])


    def backwards(self, orm):
        # Deleting model 'Report'
        db.delete_table('simple_report_report')

        # Deleting model 'Subject'
        db.delete_table('simple_report_subject')

        # Deleting model 'Subjects'
        db.delete_table('simple_report_subjects')


    models = {
        'simple_report.report': {
            'Meta': {'object_name': 'Report'},
            'course': ('django.db.models.fields.CharField', [], {'default': "'BUSINESS'", 'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone': ('django.db.models.fields.IntegerField', [], {'default': "'0243637783'", 'max_length': '10'})
        },
        'simple_report.subject': {
            'Meta': {'object_name': 'Subject'},
            'grade': ('django.db.models.fields.CharField', [], {'default': "'A'", 'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['simple_report.Report']"}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'simple_report.subjects': {
            'Meta': {'object_name': 'Subjects'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['simple_report']