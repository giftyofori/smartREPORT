# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Index'
        db.create_table('index', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.IntegerField')(max_length=10)),
        ))
        db.send_create_signal('reportcard', ['Index'])

        # Adding model 'Student'
        db.create_table('students', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('id_number', self.gf('django.db.models.fields.PositiveIntegerField')(default=100, max_length=6)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('middle_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('course', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('form', self.gf('django.db.models.fields.IntegerField')(max_length=1)),
            ('Email', self.gf('django.db.models.fields.EmailField')(max_length=50, blank=True)),
            ('phone_number', self.gf('phonenumber_field.modelfields.PhoneNumberField')(max_length=13)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('reportcard', ['Student'])

        # Adding model 'Teaches'
        db.create_table('teaches', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('teacher_id', self.gf('django.db.models.fields.IntegerField')(max_length=8)),
            ('subject_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('class_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('reportcard', ['Teaches'])

        # Adding model 'Teacher'
        db.create_table('reportcard_teacher', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('id_number', self.gf('django.db.models.fields.IntegerField')(max_length=6)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('reportcard', ['Teacher'])

        # Adding model 'Student_Info'
        db.create_table('student_info', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reportcard.Student'])),
            ('class_teacher_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reportcard.Teacher'])),
            ('course', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('mother_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('father_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('reportcard', ['Student_Info'])

        # Adding model 'Subject'
        db.create_table('subject', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('reportcard', ['Subject'])

        # Adding model 'Core_subjects'
        db.create_table('core subjects', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subject_name', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal('reportcard', ['Core_subjects'])

        # Adding model 'Course'
        db.create_table('course', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('course_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('number_student', self.gf('django.db.models.fields.IntegerField')(max_length=4)),
        ))
        db.send_create_signal('reportcard', ['Course'])

        # Adding model 'Elective_subjects'
        db.create_table('elective subjects', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subject_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reportcard.Course'])),
        ))
        db.send_create_signal('reportcard', ['Elective_subjects'])

        # Adding model 'Report'
        db.create_table('report', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('id_number_student', self.gf('django.db.models.fields.IntegerField')(max_length=10000)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('student_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('course', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('form', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
            ('teacher', self.gf('django.db.models.fields.CharField')(default='logged in user', max_length=50)),
            ('term', self.gf('django.db.models.fields.CharField')(default='First', max_length=10)),
            ('remark', self.gf('django.db.models.fields.TextField')(max_length=300)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reportcard.Student'])),
        ))
        db.send_create_signal('reportcard', ['Report'])

        # Adding model 'Report_content'
        db.create_table('report content', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('report', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reportcard.Report'])),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('exam_mark', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('test_mark', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('percentage', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('grade', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('reportcard', ['Report_content'])


    def backwards(self, orm):
        # Deleting model 'Index'
        db.delete_table('index')

        # Deleting model 'Student'
        db.delete_table('students')

        # Deleting model 'Teaches'
        db.delete_table('teaches')

        # Deleting model 'Teacher'
        db.delete_table('reportcard_teacher')

        # Deleting model 'Student_Info'
        db.delete_table('student_info')

        # Deleting model 'Subject'
        db.delete_table('subject')

        # Deleting model 'Core_subjects'
        db.delete_table('core subjects')

        # Deleting model 'Course'
        db.delete_table('course')

        # Deleting model 'Elective_subjects'
        db.delete_table('elective subjects')

        # Deleting model 'Report'
        db.delete_table('report')

        # Deleting model 'Report_content'
        db.delete_table('report content')


    models = {
        'reportcard.core_subjects': {
            'Meta': {'object_name': 'Core_subjects', 'db_table': "'core subjects'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subject_name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'reportcard.course': {
            'Meta': {'object_name': 'Course', 'db_table': "'course'"},
            'course_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number_student': ('django.db.models.fields.IntegerField', [], {'max_length': '4'})
        },
        'reportcard.elective_subjects': {
            'Meta': {'object_name': 'Elective_subjects', 'db_table': "'elective subjects'"},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['reportcard.Course']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subject_name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'reportcard.index': {
            'Meta': {'object_name': 'Index', 'db_table': "'index'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'max_length': '10'})
        },
        'reportcard.report': {
            'Meta': {'object_name': 'Report', 'db_table': "'report'"},
            'course': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'form': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_number_student': ('django.db.models.fields.IntegerField', [], {'max_length': '10000'}),
            'remark': ('django.db.models.fields.TextField', [], {'max_length': '300'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['reportcard.Student']"}),
            'student_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'teacher': ('django.db.models.fields.CharField', [], {'default': "'logged in user'", 'max_length': '50'}),
            'term': ('django.db.models.fields.CharField', [], {'default': "'First'", 'max_length': '10'})
        },
        'reportcard.report_content': {
            'Meta': {'object_name': 'Report_content', 'db_table': "'report content'"},
            'exam_mark': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'grade': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'percentage': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['reportcard.Report']"}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'test_mark': ('django.db.models.fields.IntegerField', [], {'max_length': '3'})
        },
        'reportcard.student': {
            'Email': ('django.db.models.fields.EmailField', [], {'max_length': '50', 'blank': 'True'}),
            'Meta': {'object_name': 'Student', 'db_table': "'students'"},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'course': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'form': ('django.db.models.fields.IntegerField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_number': ('django.db.models.fields.PositiveIntegerField', [], {'default': '100', 'max_length': '6'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'phone_number': ('phonenumber_field.modelfields.PhoneNumberField', [], {'max_length': '13'})
        },
        'reportcard.student_info': {
            'Meta': {'object_name': 'Student_Info', 'db_table': "'student_info'"},
            'class_teacher_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['reportcard.Teacher']"}),
            'course': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'father_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mother_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['reportcard.Student']"})
        },
        'reportcard.subject': {
            'Meta': {'object_name': 'Subject', 'db_table': "'subject'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'reportcard.teacher': {
            'Meta': {'object_name': 'Teacher'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_number': ('django.db.models.fields.IntegerField', [], {'max_length': '6'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'reportcard.teaches': {
            'Meta': {'object_name': 'Teaches', 'db_table': "'teaches'"},
            'class_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subject_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'teacher_id': ('django.db.models.fields.IntegerField', [], {'max_length': '8'})
        }
    }

    complete_apps = ['reportcard']