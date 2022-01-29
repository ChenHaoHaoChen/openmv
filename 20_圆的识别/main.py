import sensor,image,time #引入sensor,time,image模块

sensor.reset()                     #重置感光元件
sensor.set_pixformat(sensor.RGB565)#设置照片格式为RGB565，灰度图同样可以
sensor.set_framesize(sensor.QVGA)  #设置图像大小为QVGA
sensor.skip_frames()               #跳过300ms内不稳定帧数

clock = time.clock() #构造始终对象
ROI = (0,0,320,160)  #设置感兴趣区，即QVGA图像的全屏
while(True):
    clock.tick()           #开始追踪运行时间
    img = sensor.snapshot()#拍摄一张照片
    #img.lens_corr(1.8)     #形状识别需矫正镜头，或使用无畸变镜头
    #在拍摄的照片中寻找圆
    for circle in img.find_circles(roi = ROI,x_stride = 2,y_stride = 2,z_stride = 2,
    threshold = 3500,
    x_margin = 10,y_margin = 10,z_margin = 10,
    r_min = 2,r_max = 320,r_step = 2):
        img.draw_circle(circle.x(),circle.y(),circle.r())#若找到圆，则用圆圈出
        print(circle.r(),circle.magnitude()) #若找到圆，打印出圆的半径和模
    img.draw_string(0,0,"fps:%0.1f"%clock.fps(),color = (0,0,0))#用黑色在图像上显示当前帧率
