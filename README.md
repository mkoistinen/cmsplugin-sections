cmsplugin-sections
==================

This is a plugin "system" (really just two) for making "single-page scroller"
websites super easy.

It provides a Section Container plugin and a generic Section plugin out of the
box. Section Containers allow Section plugins to be added inside them. Section
plugins will allow anything inside them, but have some basic configuration of
their own, namely:

1. Title - The title of the section;

2. Show title - If unchecked, will not emit a heading for the section;

3. Label - A menu title for the section. This is by default identical to the
   title, but allows for a menu label different than the section title;

4. Show in menu - If unchecked, this section will not appear in the menu.

5. Slug - a slug. If left blank, will be derived from the title.


The Section Container will render all of its children plugins, but first, it
will emit basic menu markup of the contained sections.

Now your operators can move sections around, and the in-page menu will stay up
to date.

For your section-linking convenience, each Section plugin will also emit links
to the previous and next sections, if present.

You will need to provide some CSS styling and possibly some JS for nice,
smooth, intra-page link scrolling. I use something like this in my projects
that use jQuery:

```` Javascript
(function($){
  $(function(){
    //
    // Provide graceful scrolling around the page
    //
    $("nav.page").on('click', 'a', function(evt) {
      var $this = $(this),
          target = $this.attr('href');

      if (target[0] === '#') {
        evt.preventDefault();
        $('html,body').stop().animate({
          'scrollTop': $(target).offset().top
        }, 800, 'swing');
      }
    });
  });
}(window.jQuery));
````


## INSTALLATION

`pip install cmsplugin-sections`

Then, add 'cmsplugin_sections' to your INSTALLED_APPS.

If using Django 1.7, then add:

	'cmsplugin_sections': 'cmsplugin_sections.migrations_django'

to settings.MIGRATION_MODULES


## NORMAL USAGE

1. Add a Section Container plugin to the page;
2. Add one or more Section plugins into the Section Container;
3. Add content to each Section plugin as per usual;
4. Style with CSS to suite your needs;
5. Optionally add the above JS to your project to provide smooth scrolling
   between sections;
6. Optionally override or extend the provided templates to further suite your
   needs.


## ADVANCED USAGE

In most cases, you could easily just create normal CMS Plugins which can then
be added to a Section plugin to get the variety of content you wish your
operators to choose from. However, there may be some cases where it makes
sense to just create a custom Section plugin.

Both the Section Container and the Section plugin were built in a manner that
provides easy extention via subclassing a "base" plugin and a "base" plugin
model. This makes it pretty straightforward to create your own, pluggable
sections types for your operators.

If you plan to create your own, custom Sections for your project, your
`models.py` might looks something like this:

```` python
from django.db import models
from cmsplugin_sections.models import AbstractSectionBasePluginModel

class SplashSectionPluginModel(AbstractSectionBasePluginModel):
	#
    # Include project-specific Section Plugin configuration here. Or not. See
	# note below.
	#
    pass

````

NOTE:
	
	If is entirely optional to create your own pluginmodel if you don't need
	to add configuration options. You *could* just use the provided one, but,
	if you ever change your mind, it will be rather complicated to migrate any
	existing Section plugins to your new model. If instead you create an
	intermediate base class like the one shown above, even if its body is
	simply: `pass`, you will thank yourself in the future when you decide to
	add a configuration parameter to any existing sections of this type.


Your `cms_plugins.py` might look like this:

```` python
from cmsplugin_sections.cms_plugins import BaseSectionPlugin
# Assumes models.py and cms_plugins.py are at the same level in your project.
from .models import SplashSectionPluginModel

class SplashSectionPlugin(BaseSectionPlugin):

	# Many of these options are configurable. See source for hints.
    cache = True
    model = SplashSectionPluginModel
    name = 'Splash Section'
    render_template = "YOUR_APP/splash_section.html"

	def render_plugin(self, context, instance, placeholder):
		# Do your own thing here ...
		return context

plugin_pool.register_plugin(SplashSectionPlugin)
````
