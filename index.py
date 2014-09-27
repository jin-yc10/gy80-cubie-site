__author__ = 'jin-yc10'

import web

from sensors import gyro, accel, compass, baro

urls = (
    '/',        'index',
    '/gyro',    'gyro_handler',
    '/accel',   'accel_handler',
    '/compass', 'compass_handler',
    '/baro',    'baro_handler',
    '/sensors', 'sensor_handler'
)

gyro_sensor = gyro.L3G4200D()
compass_sensor = compass.hmc5883l()
accel_sensor = accel.ADXL345()
#baro_sensor = baro.BMP085()

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

class accel_handler:
    def GET(self):
        return str(accel_sensor.getAxes())

class baro_handler:
    def GET(self):
        return str("under construction")#baro_sensor.readAltitude())

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
