import sensor #引入sensor模块

sensor.reset() #重置感光元件
sensor.set_pixformat(sensor.RGB565) #设置照片格式为RGB565
sensor.set_framesize(sensor.QVGA) #设置图像大小为QVGA
sensor.skip_frames(time = 1000) #跳过1s内帧数

while(True):
    img = sensor.snapshot() #拍摄一张图片
    img.draw_line((10,10,30,10),color = (255,0,0))        #在(10,10)和(30,10)之间画线
    img.draw_rectangle((20,20,20,20),color = (0,255,0))   #在点(20,20)处画20*20框
    img.draw_circle(70,70,30,color = (0,0,255))           #在圆心(70,70)处画半径为30圆
    img.draw_cross(100,100,size = 15,color = (255,255,0)) #在坐标(100,100)处画尺寸为15十字
    img.draw_string(120,120,"chenhao\nhahaha",color = (255,0,255))#在坐标(120,120)处写字
                                                                #“chenhao”,并换行写“hahaha”
