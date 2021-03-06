# -*- coding: utf-8 -*-

import os
import logging
import datetime

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.api import taskqueue

from django.utils import simplejson
from pytz import timezone
import pytz

from db import UserPrefs
from db import BotPrefs
from db import BotMessage
from db import StoreTweetHistory

class UpdateUserPrefsAPI(webapp.RequestHandler):
    def post(self):
        user = users.get_current_user()
        
        user_prefs = UserPrefs.all().filter('google_account =', user).get()
        if user_prefs is None:
            return self.error(404)
        
        daily_max_notify_count = self.request.get('daily_max_notify_count')
        schedule_0000_0300 = self.request.get('0000_0300')
        schedule_0300_0600 = self.request.get('0300_0600')
        schedule_0600_0900 = self.request.get('0600_0900')
        schedule_0900_1200 = self.request.get('0900_1200')
        schedule_1200_1500 = self.request.get('1200_1500')
        schedule_1500_1800 = self.request.get('1500_1800')
        schedule_1800_2100 = self.request.get('1800_2100')
        schedule_2100_2400 = self.request.get('2100_2400')
        logging.info(schedule_2100_2400)
        
        current_timezone = timezone(self.request.get('timezone'))
        utc_timezone = timezone('UTC')
        
        #schedule = Schedule.all().filter('user_prefs_key =', user_prefs.key()).get()
        #if schedule is None:
        #    schedule = Schedule()
        schedule_list = []
        
        user_prefs.daily_max_notify_count = int(daily_max_notify_count)
        
        if schedule_0000_0300 == '1':
            user_prefs.schedule_0000_0300 = True
            utc = datetime.datetime(2011, 01, 01, 0, 0, 0, tzinfo=current_timezone)
            schedule_list.append(utc.astimezone(utc_timezone).hour)
            
            utc = datetime.datetime(2011, 01, 01, 1, 0, 0, tzinfo=current_timezone)
            schedule_list.append(utc.astimezone(utc_timezone).hour)
            
            utc = datetime.datetime(2011, 01, 01, 2, 0, 0, tzinfo=current_timezone)
            schedule_list.append(utc.astimezone(utc_timezone).hour)
        else:
            user_prefs.schedule_0000_0300 = False
        
        if schedule_0300_0600 == '1':
            user_prefs.schedule_0300_0600 = True
            
            utc = datetime.datetime(2011, 01, 01, 3, 0, 0, tzinfo=current_timezone)
            schedule_list.append(utc.astimezone(utc_timezone).hour)
            
            utc = datetime.datetime(2011, 01, 01, 4, 0, 0, tzinfo=current_timezone)
            schedule_list.append(utc.astimezone(utc_timezone).hour)
            
            utc = datetime.datetime(2011, 01, 01, 5, 0, 0, tzinfo=current_timezone)
            schedule_list.append(utc.astimezone(utc_timezone).hour)
        else:
            user_prefs.schedule_0300_0600 = False
            
        if schedule_0600_0900 == '1':
            user_prefs.schedule_0600_0900 = True
            
            utc = datetime.datetime(2011, 01, 01, 6, 0, 0, tzinfo=current_timezone)
            schedule_list.append(utc.astimezone(utc_timezone).hour)
            
            utc = datetime.datetime(2011, 01, 01, 7, 0, 0, tzinfo=current_timezone)
            schedule_list.append(utc.astimezone(utc_timezone).hour)
            
            utc = datetime.datetime(2011, 01, 01, 8, 0, 0, tzinfo=current_timezone)
            schedule_list.append(utc.astimezone(utc_timezone).hour)
        else:
            user_prefs.schedule_0600_0900 = False
            
        if schedule_0900_1200 == '1':
            user_prefs.schedule_0900_1200 = True
            
            utc = datetime.datetime(2011, 01, 01, 9, 0, 0, tzinfo=current_timezone)
            schedule_list.append(utc.astimezone(utc_timezone).hour)
            
            utc = datetime.datetime(2011, 01, 01, 10, 0, 0, tzinfo=current_timezone)
            schedule_list.append(utc.astimezone(utc_timezone).hour)
            
            utc = datetime.datetime(2011, 01, 01, 11, 0, 0, tzinfo=current_timezone)
            schedule_list.append(utc.astimezone(utc_timezone).hour)
        else:
            user_prefs.schedule_0900_1200 = False
            
        if schedule_1200_1500 == '1':
            user_prefs.schedule_1200_1500 = True
            
            utc = datetime.datetime(2011, 01, 01, 12, 0, 0, tzinfo=current_timezone)
            schedule_list.append(utc.astimezone(utc_timezone).hour)
            
            utc = datetime.datetime(2011, 01, 01, 13, 0, 0, tzinfo=current_timezone)
            schedule_list.append(utc.astimezone(utc_timezone).hour)
            
            utc = datetime.datetime(2011, 01, 01, 14, 0, 0, tzinfo=current_timezone)
            schedule_list.append(utc.astimezone(utc_timezone).hour)
        else:
            user_prefs.schedule_1200_1500 = False
            
        if schedule_1500_1800 == '1':
            user_prefs.schedule_1500_1800 = True
            
            utc = datetime.datetime(2011, 01, 01, 15, 0, 0, tzinfo=current_timezone)
            schedule_list.append(utc.astimezone(utc_timezone).hour)
            
            utc = datetime.datetime(2011, 01, 01, 16, 0, 0, tzinfo=current_timezone)
            schedule_list.append(utc.astimezone(utc_timezone).hour)
            
            utc = datetime.datetime(2011, 01, 01, 17, 0, 0, tzinfo=current_timezone)
            schedule_list.append(utc.astimezone(utc_timezone).hour)
        else:
            user_prefs.schedule_1500_1800 = False
            
        if schedule_1800_2100 == '1':
            user_prefs.schedule_1800_2100 = True
            
            utc = datetime.datetime(2011, 01, 01, 18, 0, 0, tzinfo=current_timezone)
            schedule_list.append(utc.astimezone(utc_timezone).hour)
            
            utc = datetime.datetime(2011, 01, 01, 19, 0, 0, tzinfo=current_timezone)
            schedule_list.append(utc.astimezone(utc_timezone).hour)
            
            utc = datetime.datetime(2011, 01, 01, 20, 0, 0, tzinfo=current_timezone)
            schedule_list.append(utc.astimezone(utc_timezone).hour)
        else:
            user_prefs.schedule_1800_2100 = False
            
        if schedule_2100_2400 == '1':
            user_prefs.schedule_2100_2400 = True
            
            utc = datetime.datetime(2011, 01, 01, 21, 0, 0, tzinfo=current_timezone)
            schedule_list.append(utc.astimezone(utc_timezone).hour)
            
            utc = datetime.datetime(2011, 01, 01, 22, 0, 0, tzinfo=current_timezone)
            schedule_list.append(utc.astimezone(utc_timezone).hour)
            
            utc = datetime.datetime(2011, 01, 01, 23, 0, 0, tzinfo=current_timezone)
            schedule_list.append(utc.astimezone(utc_timezone).hour)
        else:
            user_prefs.schedule_2100_2400 = False
            
        user_prefs.schedule_list = schedule_list
        user_prefs.timezone = current_timezone.zone
        
        if len(schedule_list) > 0:
            user_prefs.notify_probability = (float(user_prefs.daily_max_notify_count)  / (float(len(schedule_list)) * 6)) * 100
        else:
            user_prefs.notify_probability = 0.0
            
        user_prefs.activate_flg = True
        user_prefs.put()
        
        json = simplejson.dumps({'status': True}, ensure_ascii=False)
        self.response.content_type = 'application/json'
        self.response.out.write(json)

class UpdateBotAPI(webapp.RequestHandler):
    def post(self):
        
        user = users.get_current_user()
        
        user_prefs = UserPrefs.all().filter('google_account =', user).get()
        if user_prefs is None:
            return self.error(404)
        
        bot_id = self.request.get('bot_id')
        if bot_id == '_custom':
            custom_bot_id = self.request.get('custom_bot_id')
            bot = BotPrefs.all().filter('bot_id =', custom_bot_id).get()
            logging.info('Custom Bot ID: %s' % custom_bot_id)
        else:
            bot = BotPrefs.all().filter('bot_id =', bot_id).get()
            logging.info('Bot ID: %s' % bot_id)
            
        if bot is not None:
            user_prefs.bot_prefs_key = bot.key()
            user_prefs.put()
            
            data = {'status': True, 'bot_id': bot.bot_id, 'nickname': bot.nickname}
        else:
            logging.error('bot_id is invalid.')
            data = {'status': False, 'message': 'Bot ID is invalid.'}
            
        json = simplejson.dumps(data, ensure_ascii=False)
        self.response.content_type = 'application/json'
        self.response.out.write(json)
        
class UpdateBotAddAPI(webapp.RequestHandler):
    def post(self):
        user = users.get_current_user()
        
        bot_id = self.request.get('bot_id')
        nickname = self.request.get('nickname')
        
        if nickname == '':
            nickname = bot_id
        
        message = ''
        
        bot_prefs = BotPrefs.all().filter('bot_id =', bot_id).get()
        if bot_prefs is not None:
            message = '%s is already exists.' % bot_id
            data = {'status': False, 'message': message}
        else:
            bot_prefs = BotPrefs()
            bot_prefs.google_account = user
            bot_prefs.bot_id = bot_id
            bot_prefs.nickname = nickname
            bot_prefs.public_flg = False
            bot_prefs.delete_flg = False
            bot_prefs.put()
            
            data = {'status': True, 'message': None}
            
        
        template_values = {
            'bot_id': bot_id,
            'nickname': nickname,
            'message': message
        }
        
        json = simplejson.dumps(data, ensure_ascii=False)
        self.response.content_type = 'application/json'
        self.response.out.write(json)
        
class UpdateBotEditAPI(webapp.RequestHandler):
    def post(self):
        user = users.get_current_user()
        bot_id = self.request.get('bot_id')
        
        bot_prefs = BotPrefs.all().filter('bot_id =', bot_id).filter('google_account =', user).get()
        if bot_prefs is None:
            return self.error(404)
        
        mode = self.request.get('mode')
        if mode == 'modify':
            nickname = self.request.get('nickname')
            public_flg = self.request.get('public_flg')
            bot_prefs.nickname = nickname
            
            if public_flg == '1':
                bot_prefs.public_flg = True
            else:
                bot_prefs.public_flg = False
            
            bot_prefs.put()
            
        json = simplejson.dumps({'status': True}, ensure_ascii=False)
        self.response.content_type = 'application/json'
        self.response.out.write(json)
        
class UpdateBotAddMessageAPI(webapp.RequestHandler):
    def post(self):
        user = users.get_current_user()
        bot_id = self.request.get('bot_id')
        
        bot_prefs = BotPrefs.all().filter('bot_id =', bot_id).filter('google_account =', user).get()
        if bot_prefs is None:
            return self.error(404)
        
        mode = self.request.get('mode')
        if mode == 'add_message':
            time = self.request.get('time')
            message = self.request.get('message')
            
            logging.info('time: %s' % time)
            
            if time.find('simple_') > -1:
                logging.info('Simple mode')
                hour = int(time[7:])
                for i in range(3):
                    time = '%02d00-%02d00' % (hour, hour + 1)
                    logging.info('time: %s' % time)
                    bot_message = BotMessage()
                    bot_message.bot_prefs_key = bot_prefs.key()
                    bot_message.time = time
                    bot_message.message = message
                    bot_message.put()
                    
                    hour = hour + 1
                
            else:
                bot_message = BotMessage()
                bot_message.bot_prefs_key = bot_prefs.key()
                bot_message.time = time
                bot_message.message = message
                bot_message.put()
            
        json = simplejson.dumps({'status': True}, ensure_ascii=False)
        self.response.content_type = 'application/json'
        self.response.out.write(json)

class UpdateBotDeleteMessageAPI(webapp.RequestHandler):
    def post(self):

        user = users.get_current_user()
        bot_id = self.request.get('bot_id')
        
        bot_prefs = BotPrefs.all().filter('bot_id =', bot_id).filter('google_account =', user).get()
        if bot_prefs is None:
            return self.error(404)
        
        mode = self.request.get('mode')
        if mode == 'delete_message':
            message_id = self.request.get('message_id')
            bot_message = BotMessage.get_by_id(int(message_id))
                
            if bot_message is not None:
                advance_flg = self.request.get('advance')
                if advance_flg == 'True':
                    bot_message.delete()
                else:
                    try:
                        hour = int(self.request.get('hour'))
                        
                        for i in range(3):
                            time = '%02d00-%02d00' % (hour, hour + 1)
                            
                            bot_message_list = BotMessage.all().filter('time =', time).filter('message =', bot_message.message).fetch(20)
                            if bot_message_list is not None:
                                for row in bot_message_list:
                                    logging.info('Delete: %s -> %s' % (time, bot_message.message))
                                    row.delete()
                            
                            hour = hour + 1
                            
                    except:
                        pass
                
        json = simplejson.dumps({'status': True}, ensure_ascii=False)
        self.response.content_type = 'application/json'
        self.response.out.write(json)
        
class StoreTweetAPI(webapp.RequestHandler):
    def post(self):

        user = users.get_current_user()
        
        user_prefs = UserPrefs.all().filter('google_account =', user).get()
        if user_prefs is None:
            return self.error(404)
        
        store_tweet_history = StoreTweetHistory.all().filter('google_account =', user).filter('expired_at >', datetime.datetime.now()).get()
        if store_tweet_history is None:
            user_prefs.free_quantity = user_prefs.free_quantity + 100
            user_prefs.activate_flg = True
            user_prefs.put()
            
            store_tweet_history = StoreTweetHistory()
            store_tweet_history.google_account = user
            store_tweet_history.expired_at = datetime.datetime.now() + datetime.timedelta(days=7)
            store_tweet_history.put()
            
            data = {'status': True}
        else:
            data = {'status': False}
        
        json = simplejson.dumps(data, ensure_ascii=False)
        self.response.content_type = 'application/json'
        self.response.out.write(json)
        
class UpdateTestNotificationAPI(webapp.RequestHandler):
    def post(self):

        user = users.get_current_user()
        
        user_prefs = UserPrefs.all().filter('google_account =', user).get()
        if user_prefs is None:
            return self.error(404)
        
        try:
            bot_id = user_prefs.bot_prefs_key.key().id()
            taskqueue.add(url = '/task/find_device', params = {'user_id': user_prefs.key().id(), 'bot_id': bot_id})
            data = {'status': True}
        except:
            logging.error('Add task failed.')
            data = {'status': False}
        
        json = simplejson.dumps(data, ensure_ascii=False)
        self.response.content_type = 'application/json'
        self.response.out.write(json)
        
application = webapp.WSGIApplication(
                                     [('/api/update/user_prefs', UpdateUserPrefsAPI),
                                      ('/api/update/bot', UpdateBotAPI),
                                      ('/api/update/bot/add', UpdateBotAddAPI),
                                      ('/api/update/bot/edit', UpdateBotEditAPI),
                                      ('/api/update/bot/add_message', UpdateBotAddMessageAPI),
                                      ('/api/update/bot/delete_message', UpdateBotDeleteMessageAPI),
                                      ('/api/store/tweet', StoreTweetAPI),
                                      ('/api/update/test_notification', UpdateTestNotificationAPI)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()