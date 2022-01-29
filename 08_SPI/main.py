from pyb import I2C
i2c_2 = I2C(2,I2C.MASTER,addr = 0x12,baudrate = 400000)
test = i2c_2.is_ready(0x12) #test = False或True
i2c_2.mem_read(data,0x12,0x00)



