import sensor,time,image #引入sensor,time,image模块

sensor.reset()                     #重置感光元件
sensor.set_pixformat(sensor.RGB565)#设置照片格式为RGB565
sensor.set_framesize(sensor.QQQVGA)#设置图像大小为QQQVGA(提高帧率)
sensor.skip_frames()               #跳过300ms初始帧率

clock = time.clock()               #构建时钟对象
thresholds = (5, 70, -23, 15, -57, 0)#线性回归对象的颜色阈值

while(True):
    clock.tick() #开始追踪运行时间
    #照片二值化，阈值区域为白，其他为黑色
    img = sensor.snapshot().binary([thresholds])
    #调用线性回归函数，robust = True即使用Theil-Sen线性回归算法，速度较慢，但处理异常值性能较好
    line = img.get_regression([(100,100)],robust = True)
    if line:
        #用红色线画出线性回归得到线
        img.draw_line(line.line(),color = (255,0,0))
        #打印直线的模，直线的角度，直线的截距
        print(line.magnitude(),line.theta(),line.rho())
    img.draw_string(0,0,"fps:%0.2f"%clock.fps())#图像上显示帧率
