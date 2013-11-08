#!/usr/bin/env python

#-------------------------------------------------
# PATH to extra libraries
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lib'))


#-------------------------------------------------
# webpy and decorator for webserver oauth
import web
from oauth2client.appengine import OAuth2DecoratorFromClientSecrets
from oauth2client_webpy_bridge import FakeWebapp2RequestHandler

#-------------------------------------------------
# Setting up the OAuth2 authorization and google-
#  api-interfaces
decorator = OAuth2DecoratorFromClientSecrets(
                os.path.join(os.path.dirname(__file__), 'client_secrets.json'),
                scope=['https://www.googleapis.com/auth/drive',
                       'https://www.googleapis.com/auth/calendar',
                       'https://spreadsheets.google.com/feeds'])

from apgooglelayer.drive import GoogleDrive
from apgooglelayer.calendar import GoogleCalendar
from apgooglelayer.spreadsheets import GoogleSpreadsheets

GoogleDrive = GoogleDrive()
GoogleCalendar = GoogleCalendar()
GoogleSpreadsheets = GoogleSpreadsheets()


#-------------------------------------------------
# debugging
import traceback
def printerrors(prefix):
    def thedecorator(f):
        def mydecorator(*args,**kwargs):
            try:
                return f(*args, **kwargs)
            except Exception as e:
                sp = '%s\n%s\n' % (prefix, '~'*len(prefix))
                se = 'ERROR: %s\n' % str(e)
                st = traceback.format_exc().strip().replace('\n', '\n> ')
                web.header('Content-Type', 'text/plain')
                ret = '%s\n%s\n%s' % (sp, se, st)
                return ret
        return mydecorator
    return thedecorator



#-------------------------------------------------
# GAE App

render = web.template.render('templates/')

class Index(FakeWebapp2RequestHandler):
    
    @printerrors('Indexpage Errors')
    @decorator.oauth_required 
    def GET(self):
        http = decorator.http()
        tree = GoogleDrive.folder_structure(http=http, fields='items(iconLink)')
        return render.index(tree)

class Calendar(FakeWebapp2RequestHandler):
    
    @printerrors('Calendarpage Errors')
    @decorator.oauth_required 
    def GET(self):
        http = decorator.http()
        cals = GoogleCalendar.list_calendars(http=http, fields='items(id,summary)')
        return render.cals(cals)

class Spreadsheet(FakeWebapp2RequestHandler):
    
    @printerrors('Spreadsheetpage Errors')
    @decorator.oauth_required 
    def GET(self):
        http = decorator.http()
        ssid = web.input(ssid=None).ssid
        try:
            cells = GoogleSpreadsheets.get_cells_from_first_worksheet(ssid, http=http)
        except:
            web.header('Content-Type', 'text/plain')
            raise
            return "bah"
        return render.spread(cells)


urls = ("/",                "Index",
        "/calendar",        "Calendar",
        "/spreadsheets",     "Spreadsheet",
       )

application = web.application(urls, globals()).wsgifunc()

appoauth = decorator.callback_application()







