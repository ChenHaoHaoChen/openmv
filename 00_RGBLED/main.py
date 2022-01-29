from pyb import LED,delay        #导入pyb中LED与delay

red = LED(1)  #LED(1)即红灯
green = LED(2)#LED(2)即绿灯
blue = LED(3) #LED(3)即蓝灯
t_1s = 1000       #定时时间1s

while(True):
    #红灯亮1s
    red.on()       #开红灯
    delay(t_1s)#延时1s
    red.off()      #关红灯
    #绿灯亮1s
    green.on()     #开绿灯
    delay(t_1s)#延时1s
    green.off()    #关绿灯
    #蓝灯亮1s
    blue.on()      #开蓝灯
    delay(t_1s)#延时1s
    blue.off()     #关蓝灯
    #黄灯亮1s
    red.on()       #开红灯
    green.on()     #开绿灯
    delay(t_1s)#延时1s
    red.off()      #关红灯
    green.off()    #关绿灯
    #紫灯亮1s
    red.on()       #开红灯
    blue.on()      #开蓝灯
    delay(t_1s)#延时1s
    red.off()      #关红灯
    blue.off()     #关蓝灯
    #青灯亮1s
    green.on()     #开绿灯
    blue.on()      #开蓝灯
    delay(t_1s)#延时1s
    green.off()    #关绿灯
    blue.off()     #关蓝灯
    #白灯亮1s
    red.on()       #开红灯
    green.on()     #开绿灯
    blue.on()      #开蓝灯
    delay(t_1s)#延时1s
    red.off()      #关红灯
    green.off()    #关绿灯
    blue.off()     #关蓝灯


