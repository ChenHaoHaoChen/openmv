import sensor,time,image #引入sensor,time,image模块

sensor.reset()                        #重置感光元件
sensor.set_pixformat(sensor.GRAYSCALE)#设置照片为灰度图
sensor.set_framesize(sensor.QVGA)     #设置图像格式为QVGA
sensor.skip_frames()                  #跳过300ms内帧数

clock_1 = time.clock()                #构造时钟对象

while(True):
    clock_1.tick()         #开始追踪运行时间
    img = sensor.snapshot()#拍摄一张照片
    img.lens_corr(1.8)     #对于二维码需矫正镜头畸变，或使用无畸变镜头
    #使用find_qrcodes函数找寻待检测二维码
    for qrcodes in img.find_qrcodes():
        img.draw_rectangle(qrcodes.rect())#用矩形框框出二维码
        message = qrcodes.payload()       #读取二维码中字符串信息
        print(message)                   #打印字符串中信息
    img.draw_string(0,0,"fps:%0.2f"%clock_1.fps())#在图像上打印当前帧率
