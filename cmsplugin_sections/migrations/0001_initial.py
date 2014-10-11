# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='SectionBasePluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('section_title', models.CharField(default='', help_text='This is the section title.', max_length=64, verbose_name='title')),
                ('show_title', models.BooleanField(default=True, verbose_name='display title?')),
                ('section_menu_label', models.CharField(default='', help_text='This is how the menu item is displayed. Leave empty to use section title.', max_length=64, verbose_name='label', blank=True)),
                ('section_menu_slug', models.SlugField(default='', max_length=64, blank=True, help_text='This is the hash part of the URL for intra-page links. Leave it blank and it will be auto-generated from the section title.', verbose_name='section menu slug')),
                ('show_in_menu', models.BooleanField(default=True, verbose_name='show in menu?')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='SectionContainerPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('subordinate_page', models.BooleanField(default=False, verbose_name='subordinate_page?')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
