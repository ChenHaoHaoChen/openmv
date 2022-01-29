import sensor  #引入sensor感光元件模块，sensor意为传感器
from pyb import delay
import time #引入time模块
sensor.reset()                     #初始化感光元件
sensor.set_pixformat(sensor.RGB565)#设置找照片格式为彩色
sensor.set_framesize(sensor.QVGA)  #设置图像大小为QVGA格式
#########以下代码一般可不加########
#sensor.set_auto_gain(True)     #打开自动增益（颜色识别时需关闭）
#sensor.set_auto_whitebal(True) #打开白平衡（颜色识别时需关闭）
#sensor.set_auto_exposure(True) #打开自动曝光
#sensor.set_windowing((100,100))#选取感兴趣区
#sensor.set_hmirror(False)      #取消水平翻转
#sensor.set_vflip(False)        #取消垂直翻转
################################
sensor.skip_frames(time = 1000)#跳过启动后1秒内照片

clock_1 = time.clock()  #构造时钟

while(True):
    clock_1.tick() #开始追踪运行时间
    img = sensor.snapshot() #拍摄一张照片
    print(clock_1.fps(),clock_1.avg())  #停止追踪运行时间并返回fps和平均运行时间


