from pyb import Pin,Timer,LED,delay  #引入pyb模块中Pin,Timer,LED,delay

blue = LED(3)  #选择RGB灯中blue色

def tick(timer):
    blue.toggle()  #切换LED的开关，若LED已开则关闭，若LED已关则打开

tim2 = Timer(2,freq = 5)  #选择定时器2，并以5hz触发，即每200ms触发一次
tim2.callback(tick)  #触发定时器2中断，调用tick函数

while(True):
    delay(1000)
