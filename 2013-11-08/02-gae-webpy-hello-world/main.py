#!/usr/bin/env python

# PATH to extra libraries
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lib'))

import web


class MainPage(object):
    
    def GET(self):
        web.header('Content-Type', 'text/plain')
        return 'Hello, World!'



render = web.template.render('templates/')

class TemplatedPage(object):
    
    def GET(self):
        data = web.input(data=[]).data
        return render.templateexample(data)


urls = ("/",                "MainPage",
        "/templateexample", "TemplatedPage",
       )

application = web.application(urls, globals()).wsgifunc()

