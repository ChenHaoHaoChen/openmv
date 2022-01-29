from pyb import Pin,Timer,delay  #引入pyb模块中Pin,Timer,delay

tim4 = Timer(4,freq = 1000)  #选择定时器4，并以5hz触发
#P7作通道1，输出占空比为10%的PWM方波
ch1 = tim4.channel(1,Timer.PWM,pin = Pin('P7'),pulse_width_percent = 10)
#P8作通道2，输出占空比为20%的PWM方波
ch2 = tim4.channel(2,Timer.PWM,pin = Pin('P8'),pulse_width_percent = 20)

while(True):
    delay(100)

