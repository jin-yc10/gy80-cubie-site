__author__ = 'jin-yc10'

# L3G4200D Gyro interface in python, using I2C.
from time import sleep
#import smbus to access i2c port
import smbus
import string

#converts 16 bit two's compliment reading to signed int
def getSignedNumber(number):
    if number & (1 << 15):
        return number | ~65535
    else:
        return number & 65535

class L3G4200D:
    i2c_address=0x69
    def __init__(self, i2c_ch=1):
        self.i2c_bus = smbus.SMBus(i2c_ch)
        #normal mode and all axes on to control reg1
        self.i2c_bus.write_byte_data(self.i2c_address, 0x20, 0x0F)
        #full 2000dps to control reg4
        self.i2c_bus.write_byte_data(self.i2c_address, 0x23, 0x20)

    def read(self):
        self.i2c_bus.write_byte(self.i2c_address, 0x28)
        X_L = self.i2c_bus.read_byte(self.i2c_address)
        self.i2c_bus.write_byte(self.i2c_address, 0x29)
        X_H = self.i2c_bus.read_byte(self.i2c_address)
        X = X_H << 8 | X_L

        self.i2c_bus.write_byte(self.i2c_address, 0x2A)
        Y_L = self.i2c_bus.read_byte(self.i2c_address)
        self.i2c_bus.write_byte(self.i2c_address, 0x2B)
        Y_H = self.i2c_bus.read_byte(self.i2c_address)
        Y = Y_H << 8 | Y_L

        self.i2c_bus.write_byte(self.i2c_address, 0x2C)
        Z_L = self.i2c_bus.read_byte(self.i2c_address)
        self.i2c_bus.write_byte(self.i2c_address, 0x2D)
        Z_H = self.i2c_bus.read_byte(self.i2c_address)
        Z = Z_H << 8 | Z_L

        X = getSignedNumber(X)
        Y = getSignedNumber(Y)
        Z = getSignedNumber(Z)
        return (X,Y,Z)