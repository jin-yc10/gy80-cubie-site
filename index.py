__author__ = 'jin-yc10'

import web

from sensors import gyro, accel, compass, baro

urls = (
    '/',        'index',
    '/gyro',    'gyro_handler',
    '/accel',   'accel_handler',
    '/baro',    'baro_handler'
)

class index:
    def GET(self):
        print "hello world"
        return "hello world"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()