from pyb import Pin,LED,delay  #导入pyb中Pin,LED,delay模块

p0_out = Pin('P0',Pin.OUT_PP)  #设置P0引脚为输出引脚
p1_in = Pin('P1',Pin.IN,Pin.PULL_UP)  #设置P1引脚为输入引脚

red = LED(1)
green = LED(2)

while(True):
    #P0作输出引脚
    p0_out.high()  #P0引脚输出1（3.3V）
    delay(1000)#延时1s
    p0_out.low()   #P0引脚输出0（0V）
    delay(1000)#延时1s
    #P1作输入引脚
    value = p1_in.value()#读取P1引脚电平1（3.3V）或0（0V）
    print(value)
    if value == 1:       #P1为高电平时，打开红灯
        green.off()
        red.on()
    elif value == 0:     #P1为低电平时，打开绿灯
        red.off()
        green.on()
