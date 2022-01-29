import sensor,time,image #引入sensor,time,image模块
from math import sqrt    #从math引入sqrt函数(开平方函数)

sensor.reset()                     #重置感光元件
sensor.set_pixformat(sensor.RGB565)#设置图照片格式为RGB565
sensor.set_framesize(sensor.QVGA)  #设置图像大小为QVGA(320*160)
sensor.skip_frames()               #跳过300ms内初始帧数

clock = time.clock()   #构造时钟对象
ROI_all = (0,0,320,160)#设置感兴趣区，即全屏，若不设置，图像会很卡
while(True):
    clock.tick()           #开始追踪运行时间
    img = sensor.snapshot()#拍摄一张照片
    #img.lens_corr(1.8)
    #在图像中寻找圆
    for circle in img.find_circles(roi = ROI_all,x_stride = 2,y_stride = 2,z_stride = 2,
                               threshld = 3500,
                               x_margin = 10,y_margin = 10,z_margin = 10,
                               r_min = 2,r_max = 160,r_step = 2):
        #取找到的圆的内的最大正方形
        area = (circle.x()-int((sqrt(2)/2)*circle.r()), circle.y()-int((sqrt(2)/2)*circle.r()),
                int(sqrt(2)*circle.r()), int(sqrt(2)*circle.r()))
        #统计最大正方形
        statistics = img.get_statistics(roi = area)
        #若最大正方形为红色，则认为该圆为红色，用红色的圆圈出整个圆
        if 0<statistics.l_mode()<100 and 0<statistics.a_mode()<120 and 0<statistics.b_mode()<120:
            img.draw_circle(circle.x(),circle.y(),circle.r(),color = (255,0,0))
        #否则用矩形框框出该对象
        else:
            img.draw_rectangle(area)
    #打印当前帧率
    print(clock.fps())


