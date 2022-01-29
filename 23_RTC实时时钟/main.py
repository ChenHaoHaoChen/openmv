import pyb     #引入pyb模块
rtc = pyb.RTC()#创建RTC实时时钟
#2022年1月19日周三，18时5分0秒0亚秒
rtc.datetime((2022,1,19,3,18,5,0,0))
while(True):
    print(rtc.datetime())#打印当前RTC时钟时间
    pyb.delay(1000)
