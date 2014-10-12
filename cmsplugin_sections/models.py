# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible  #, force_text
from django.utils.translation import ugettext_lazy as _

from .unique_slugify import unique_slugify

from cms.models import CMSPlugin


class AbstractSectionContainerPluginModel(CMSPlugin):
    class Meta:
        abstract = True
    pass


class SectionContainerPluginModel(AbstractSectionContainerPluginModel):
    subordinate_page = models.BooleanField(_('subordinate_page?'), default=False)


@python_2_unicode_compatible
class AbstractSectionBasePluginModel(CMSPlugin):
    """
    Defines a common interface for section plugins.
    """

    class Meta:
        abstract = True

    taints_cache = True

    section_title = models.CharField(_('title'),
        blank=False,
        default='',
        help_text=_('This is the section title.'),
        max_length=64,
    )

    show_title = models.BooleanField(_('display title?'),
        default=True,
    )

    section_menu_label = models.CharField(_('label'),
        blank=True,
        default='',
        help_text=_('This is how the menu item is displayed. Leave empty to use section title.'),
        max_length=64,
    )

    section_menu_slug = models.SlugField(_('section menu slug'),
        blank=True,
        default='',
        help_text=_('This is the hash part of the URL for intra-page links. Leave it blank and it will be auto-generated from the section title.'),
        max_length=64,
    )

    show_in_menu = models.BooleanField(_('show in menu?'),
        default=True,
    )


    def save(self, *args, **kwargs):
        """
        Save override to ensure that there is a unique slug for this item.
        """

        if not self.section_menu_label:
            self.section_menu_label = self.section_title

        if not self.section_menu_slug:
            unique_slugify(self, self.section_title, slug_field_name='section_menu_slug')

        super(AbstractSectionBasePluginModel, self).save(*args, **kwargs)


    def __str__(self):
        return self.section_menu_label


class SectionBasePluginModel(AbstractSectionBasePluginModel):
    """
    Defines a common interface for section plugins.
    """
    
    taints_cache = True
