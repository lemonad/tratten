# -*- coding: utf-8 -*-

from south.db import db
from django.db import models
from tratten.issues.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Changing field 'Issue.description'
        # (to signature: django.db.models.fields.TextField())
        db.alter_column('issues_issue', 'description', orm['issues.issue:description'])
        
        # Changing field 'Issue.reporter_phone'
        # (to signature: django.db.models.fields.CharField(max_length=32, null=True, blank=True))
        db.alter_column('issues_issue', 'reporter_phone', orm['issues.issue:reporter_phone'])
        
    
    
    def backwards(self, orm):
        
        # Changing field 'Issue.description'
        # (to signature: django.db.models.fields.TextField(blank=True))
        db.alter_column('issues_issue', 'description', orm['issues.issue:description'])
        
        # Changing field 'Issue.reporter_phone'
        # (to signature: django.db.models.fields.CharField(max_length=32, null=True))
        db.alter_column('issues_issue', 'reporter_phone', orm['issues.issue:reporter_phone'])
        
    
    
    models = {
        'categories.category': {
            'changed_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True', 'db_index': 'True'})
        },
        'issues.issue': {
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['categories.Category']"}),
            'changed_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'due_date': ('django.db.models.fields.DateField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reporter_email': ('django.db.models.fields.EmailField', [], {'max_length': '64', 'db_index': 'True'}),
            'reporter_name': ('django.db.models.fields.CharField', [], {'max_length': '48', 'db_index': 'True'}),
            'reporter_phone': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'summary': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_index': 'True'}),
            'urgent': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True', 'blank': 'True'})
        }
    }
    
    complete_apps = ['issues']
