__author__ = 'jin-yc10'

import web
import time

urls = (
    '/',        'index',
    '/sensor',  'sensor',
)

ISOTIMEFORMAT = '%Y-%m-%d %X'

render = web.template.render('templates')
class index:
    def GET(self):
        return web.template.frender('static/index.html')()

class sensor:
    def GET(self):
        return time.strftime( ISOTIMEFORMAT, time.localtime() );

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
