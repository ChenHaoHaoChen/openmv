from pyb import Servo,delay  #导入pyb中Servo,delay模块

s1 = Servo(1)   #舵机1信号线，即P7引脚
s2 = Servo(2)   #舵机2信号线，即P8引脚

while(True):

    s1.angle(0) #舵机1转动0度
    delay(500)  #延时0.5s
    s1.angle(45)#舵机1转动45度
    delay(500)  #延时0.5s
    s1.angle(90)#舵机1转动90度
    delay(500)  #延时0.5s

    s2.angle(0)
    delay(500)
    s2.angle(-45)
    delay(500)
    s2.angle(-90)
    delay(500)

    s1.angle(0) #s1复位
    s2.angle(0) #s2复位
