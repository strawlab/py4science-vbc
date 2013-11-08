#!/usr/bin/env python

import web
import urlparse

class _FakeWebObOut(object):
    def __init__(self):
        self._buffer = ''
    def write(self, x):
        self._buffer += x

class _FakeWebObResponse(object):
    def __init__(self):
        self.out = _FakeWebObOut()

class _FakeWebObRequest(object):
    @property
    def url(self):
        return web.ctx.home + web.ctx.fullpath
    @property
    def uri(self):
        return web.ctx.home + web.ctx.fullpath
    def relative_url(self, x):
        return urlparse.urljoin(self.uri, x)

class FakeWebapp2RequestHandler(object):

    def __init__(self):
        if hasattr(self, 'GET'):
            def hack(f):
                def nGET(*args, **kwargs):
                    tmp = f(*args, **kwargs)
                    if self.response.out._buffer:
                        return tmp + self.response.out._buffer
                    else:
                        return tmp
                return nGET
            self.GET = hack(self.GET)

    response = _FakeWebObResponse()
    request = _FakeWebObRequest()

    def redirect(self, x):
        web.seeother(x)

