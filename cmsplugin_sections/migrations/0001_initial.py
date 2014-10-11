# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SectionContainerPluginModel'
        db.create_table(u'cmsplugin_sections_sectioncontainerpluginmodel', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('subordinate_page', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'cmsplugin_sections', ['SectionContainerPluginModel'])

        # Adding model 'SectionBasePluginModel'
        db.create_table(u'cmsplugin_sections_sectionbasepluginmodel', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('section_title', self.gf('django.db.models.fields.CharField')(default=u'', max_length=64)),
            ('show_title', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('section_menu_label', self.gf('django.db.models.fields.CharField')(default=u'', max_length=64, blank=True)),
            ('section_menu_slug', self.gf('django.db.models.fields.SlugField')(default=u'', max_length=64, blank=True)),
            ('show_in_menu', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'cmsplugin_sections', ['SectionBasePluginModel'])


    def backwards(self, orm):
        # Deleting model 'SectionContainerPluginModel'
        db.delete_table(u'cmsplugin_sections_sectioncontainerpluginmodel')

        # Deleting model 'SectionBasePluginModel'
        db.delete_table(u'cmsplugin_sections_sectionbasepluginmodel')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        },
        u'cmsplugin_sections.sectionbasepluginmodel': {
            'Meta': {'object_name': 'SectionBasePluginModel'},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'section_menu_label': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '64', 'blank': 'True'}),
            'section_menu_slug': ('django.db.models.fields.SlugField', [], {'default': "u''", 'max_length': '64', 'blank': 'True'}),
            'section_title': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '64'}),
            'show_in_menu': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'show_title': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'cmsplugin_sections.sectioncontainerpluginmodel': {
            'Meta': {'object_name': 'SectionContainerPluginModel'},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'subordinate_page': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['cmsplugin_sections']