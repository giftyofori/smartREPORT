# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Report.student'
        db.alter_column('report', 'student_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reportcard.Student'], null=True))
        # Adding field 'Student.created_on'
        db.add_column('students', 'created_on',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 3, 1, 0, 0), blank=True),
                      keep_default=False)

        # Adding unique constraint on 'Student', fields ['id_number']
        db.create_unique('students', ['id_number'])


    def backwards(self, orm):
        # Removing unique constraint on 'Student', fields ['id_number']
        db.delete_unique('students', ['id_number'])


        # Changing field 'Report.student'
        db.alter_column('report', 'student_id', self.gf('django.db.models.fields.related.ForeignKey')(default=datetime.datetime(2013, 3, 1, 0, 0), to=orm['reportcard.Student']))
        # Deleting field 'Student.created_on'
        db.delete_column('students', 'created_on')


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
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['reportcard.Student']", 'null': 'True', 'blank': 'True'}),
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
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'form': ('django.db.models.fields.IntegerField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_number': ('django.db.models.fields.PositiveIntegerField', [], {'default': '104', 'unique': 'True', 'max_length': '6'}),
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