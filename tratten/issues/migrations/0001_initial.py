# -*- coding: utf-8 -*-

from south.db import db
from django.db import models
from tratten.issues.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Issue'
        db.create_table('issues_issue', (
            ('id', orm['issues.Issue:id']),
            ('category', orm['issues.Issue:category']),
            ('summary', orm['issues.Issue:summary']),
            ('description', orm['issues.Issue:description']),
            ('urgent', orm['issues.Issue:urgent']),
            ('due_date', orm['issues.Issue:due_date']),
            ('reporter_name', orm['issues.Issue:reporter_name']),
            ('reporter_email', orm['issues.Issue:reporter_email']),
            ('reporter_phone', orm['issues.Issue:reporter_phone']),
            ('created_at', orm['issues.Issue:created_at']),
            ('changed_at', orm['issues.Issue:changed_at']),
        ))
        db.send_create_signal('issues', ['Issue'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Issue'
        db.delete_table('issues_issue')
        
    
    
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
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'due_date': ('django.db.models.fields.DateField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reporter_email': ('django.db.models.fields.EmailField', [], {'max_length': '64', 'db_index': 'True'}),
            'reporter_name': ('django.db.models.fields.CharField', [], {'max_length': '48', 'db_index': 'True'}),
            'reporter_phone': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True'}),
            'summary': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_index': 'True'}),
            'urgent': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True', 'blank': 'True'})
        }
    }
    
    complete_apps = ['issues']
