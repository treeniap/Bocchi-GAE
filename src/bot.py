# -*- coding: utf-8 -*-

import os

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from google.appengine.api import users

from db import BotMessage
from db import BotPrefs

os.environ['DJANGO_SETTINGS_MODULE'] = 'conf.settings'
from django.conf import settings
# Force Django to reload settings
settings._target = None

from i18NRequestHandler import I18NRequestHandler

class HomePage(I18NRequestHandler):
    def get(self):

        template_values = {
        }
        
        path = os.path.join(os.path.dirname(__file__), 'templates/bot/index.html')
        self.response.out.write(template.render(path, template_values))

class ListPage(I18NRequestHandler):
    def get(self):
        user = users.get_current_user()
        
        bot_list = BotPrefs.all().filter('google_account =', user).fetch(20)

        template_values = {
            'bot_list': bot_list
        }
        
        path = os.path.join(os.path.dirname(__file__), 'templates/bot/list.html')
        self.response.out.write(template.render(path, template_values))

class EditPage(I18NRequestHandler):
    def get(self):

        bot_id = self.request.get('bot_id')
        
        bot_prefs = BotPrefs.all().filter('bot_id =', bot_id).get()
        if bot_prefs is None:
            return self.error(404)
        
        template_values = {
            'bot_id': bot_id,
            'nickname': bot_prefs.nickname,
            'public_flg': bot_prefs.public_flg,
        }
        
        path = os.path.join(os.path.dirname(__file__), 'templates/bot/edit.html')
        self.response.out.write(template.render(path, template_values))

class ScheduleListPage(I18NRequestHandler):
    def get(self):

        bot_id = self.request.get('bot_id')
        
        bot_prefs = BotPrefs.all().filter('bot_id =', bot_id).get()
        if bot_prefs is None:
            return self.error(404)
        
        bot_message_list_01 = BotMessage.all().filter('bot_prefs_key =', bot_prefs.key()).filter('time =', '0000-0300').order('created_at').fetch(20)
        bot_message_list_02 = BotMessage.all().filter('bot_prefs_key =', bot_prefs.key()).filter('time =', '0300-0600').order('created_at').fetch(20)
        bot_message_list_03 = BotMessage.all().filter('bot_prefs_key =', bot_prefs.key()).filter('time =', '0600-0900').order('created_at').fetch(20)
        bot_message_list_04 = BotMessage.all().filter('bot_prefs_key =', bot_prefs.key()).filter('time =', '0900-1200').order('created_at').fetch(20)
        bot_message_list_05 = BotMessage.all().filter('bot_prefs_key =', bot_prefs.key()).filter('time =', '1200-1500').order('created_at').fetch(20)
        bot_message_list_06 = BotMessage.all().filter('bot_prefs_key =', bot_prefs.key()).filter('time =', '1500-1800').order('created_at').fetch(20)
        bot_message_list_07 = BotMessage.all().filter('bot_prefs_key =', bot_prefs.key()).filter('time =', '1800-2100').order('created_at').fetch(20)
        bot_message_list_08 = BotMessage.all().filter('bot_prefs_key =', bot_prefs.key()).filter('time =', '2100-2400').order('created_at').fetch(20)
        
        template_values = {
            'bot_id': bot_id,
            'nickname': bot_prefs.nickname,
            'public_flg': bot_prefs.public_flg,
            'bot_message_list_01': bot_message_list_01,
            'bot_message_list_02': bot_message_list_02,
            'bot_message_list_03': bot_message_list_03,
            'bot_message_list_04': bot_message_list_04,
            'bot_message_list_05': bot_message_list_05,
            'bot_message_list_06': bot_message_list_06,
            'bot_message_list_07': bot_message_list_07,
            'bot_message_list_08': bot_message_list_08
        }
        
        path = os.path.join(os.path.dirname(__file__), 'templates/bot/schedule_list.html')
        self.response.out.write(template.render(path, template_values))

class AddMessagePage(I18NRequestHandler):
    def get(self):

        bot_id = self.request.get('bot_id')
        
        bot_prefs = BotPrefs.all().filter('bot_id =', bot_id).get()
        if bot_prefs is None:
            return self.error(404)
        
        template_values = {
            'bot_id': bot_id,
        }
        
        path = os.path.join(os.path.dirname(__file__), 'templates/bot/add_message.html')
        self.response.out.write(template.render(path, template_values))
    
class AddPage(I18NRequestHandler):
    def get(self):

        template_values = {
        }
        
        path = os.path.join(os.path.dirname(__file__), 'templates/bot/add.html')
        self.response.out.write(template.render(path, template_values))
    
application = webapp.WSGIApplication(
                                     [('/bot/', HomePage),
                                      ('/bot/add', AddPage),
                                      ('/bot/list', ListPage),
                                      ('/bot/edit', EditPage),
                                      ('/bot/schedule_list', ScheduleListPage),
                                      ('/bot/add_message', AddMessagePage)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()