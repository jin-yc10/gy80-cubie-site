__author__ = 'jin-yc10'

import web

from sensors import gyro, accel, compass, baro

urls = (
    '/',        'index',
    '/gyro',    'gyro_handler',
    '/accel',   'accel_handler',
    '/compass', 'compass_handler',
    '/baro',    'baro_handler'
)

gyro_sensor = gyro.L3G4200D()
compass_sensor = compass.hmc5883l()

class index:
    def GET(self):
        print "hello world"
        return "hello world"

class gyro_handler:
    def GET(self):
        return str(gyro_sensor.read())

class compass_handler:
    def GET(self):
        return str(compass_sensor.axes())

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()