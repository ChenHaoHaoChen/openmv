import sensor,time,image  #引入sensor,time模块

sensor.reset() #初始化感光元件
sensor.set_pixformat(sensor.RGB565)#设置照片格式为RGB565
sensor.set_framesize(sensor.QQVGA)  #设置图像大小为QQVGA(23帧),若设置为QVGA则很卡，帧数只有7帧

sensor.set_auto_gain(False)    #关闭自动增益
sensor.set_auto_whitebal(False)#关闭白平衡

sensor.skip_frames(time = 1000)#跳过1s的帧数

clock_1 = time.clock() #构造时钟对象

while(True):
    clock_1.tick() #开始追踪运行时间
    img = sensor.snapshot() #拍摄一张照片
    for apriltags in img.find_apriltags():
        img.draw_rectangle(apriltags.rect(),color = (255,0,0)) #用红色框框出Apriltags
        img.draw_cross(apriltags.cx(),apriltags.cy(),color = (0,255,0)) #在框中央画上绿色十字
        degress = apriltags.rotation()*180/3.14 #求出AprilTag旋转角度
        #AprilTag标签的ID；旋转角度；AprilTag四个角坐标，依次为左上角顺时针取
        print(apriltags.id(),degress,apriltags.corners())
    print(clock_1.fps()) #打印当前帧数
