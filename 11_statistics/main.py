import sensor #引入sensor模块

sensor.reset() #重置感光元件
sensor.set_pixformat(sensor.RGB565) #设置照片格式为RGB65
sensor.set_framesize(sensor.QVGA)   #设置照片大小为QVGA
sensor.skip_frames(time = 1000)     #跳过1s内帧数
ROI = (120,160,50,50)      #选取（120，160）坐标处宽50高50的感兴趣区
while(True):
    img = sensor.snapshot()#拍摄一张图像
    Statistics = img.get_statistics(roi = ROI) #获取感兴趣的统计信息
    color_l = Statistics.mode() #获取感兴趣区L通道上众数
    color_a = Statistics.mode() #获取感兴趣区A通道上众数
    color_b = Statistics.mode() #获取感兴趣区B通道上众数
    img.draw_rectangle(ROI)     #在图像上用框画出感兴趣区
    print(color_l,color_a,color_b) #打印出L、A、B通道上众数
