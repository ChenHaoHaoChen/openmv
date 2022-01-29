from pyb import DAC,Pin,delay  #从pyb模块中引入Pin,DAC,delay
dac_p6 = DAC('P6')  #设置P6引脚为数模转换引脚
#产生三角波
while(True):
    for i in range(256):
        dac_p6.write(i)  #输出电压，范围为：0~255，即：0~3.3V
        print((i*3.3)/256)
        delay(5)
    for i in range(256):
        dac_p6.write(255-i)
        print((255-i)*3.3/256)
        delay(5)
